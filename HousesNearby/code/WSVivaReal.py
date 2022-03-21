from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import math
from datetime import datetime

from WSDataManager import WSDataManager

# ========== THIS OPTIONS IS TO BE USED ON business VARIABLE ===========
# OPTIONS
# 1 - COMPRAR
# 2 - ALUGAR
# 3 - IMOVEIS NOVOS

# ========== THIS OPTIONS TYPE IS TO BE USED ON type VARIABLE ==========
# OPTIONS TYPE
# 1 - Mostrar todos
# Residencial
# 2 - Apartamento
# 3 - Casa de Condominio
# 4 - Characa
# 5 - Cobertura
# 6 - Flat
# 7 - Kitnet/Conjudago
# 8 - Lote/Terreno
# 9 - Sobrado
# 10 - Edificio Residencial
# 11 - Fazenda/Sítio/Chácaras
# Comercial
# 12 - Consultório
# 13 - Galpao/Deposito/Armazém
# 14 - Imóvel Comercial
# 15 - Lote/Terreno
# 16 - Ponto Comercial/Loja/Box
# 17 - Sala/Conjunto


class WSVivaReal():
    def __init__(self, city, neighborhood, DEBUG, business=2, type=2, local="Santa Felicidade, Curitiba - PR"):
        self.url = None
        self.driver = None
        self.business = business-1
        self.type = type-1
        self.local = local
        self.result_list = []
        self.neighborhood = neighborhood
        self.city = city

        self.data_manager = WSDataManager("data_vivareal")

        self.columns = ["id", "url", "address", "area", "rooms", "batrooms", "garage", "amenities", "value", "condominium", "date"]

        self.DEBUG = DEBUG

        if business == 1:
            self.business_type = "venda"
        elif business == 2:
            self.business_type = "aluguel"
        else:
            self.business_type = "condominio"

    # INITIALIZE FUNCTION
    def initilize(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    # OPEN THE CURRENT neighborhood TO SEARCH
    def goToUrl(self, neighborhood):
        self.url = f"https://www.vivareal.com.br/{self.business_type}/parana/{self.city}//bairros/{neighborhood}//apartamento_residencial/"
        self.driver.get(self.url)

        time.sleep(5)

    # RETURN THE RESULT LIST WITH ALL ITENS
    def getResultList(self):
        return self.result_list

    def log(self, message, level=1):
        if self.DEBUG:
            if level <= self.DEBUG:
                print(message)


    # GET DATA FROM THE MAIN WEB PAGE
    # HERE WE NEED TO ADD THE BUSINES TYPE AND THE TYPE OF PROPERTY AND THE LOCALIZATION
    def setFirstPage(self):
        # GET THE SEARCH BAR DROP DOWN ITEM
        search_bar_selector = self.driver.find_element_by_class_name("main-search__select-fields")

        # GET THE BUSINES ITEM
        business_type_drop_dow = search_bar_selector.find_element_by_class_name("js-select-business")
        # SET TO CHOOSE TYPE
        business_type_drop_dow.find_elements_by_tag_name("option")[self.business].click()

        # GET THE TYPE PROPERTY ITEM
        type_drop_dow = search_bar_selector.find_element_by_class_name("js-select-type")
        # GET THE TWO PPOSSIBLE SUB ITENS "Residencial" OR "Comercial"
        comertial_type_list = type_drop_dow.find_elements_by_tag_name("optgroup")

        type_list = None

        # CORRECT SELECT THE CHOOSE ITEM AND CORRECT THE INDEX
        # IF self.type == 0 THE THE ITEM IS "Mostrar Todos"
        if self.type == 0:
            type_drop_dow.find_element_by_tag_name("option").click()

        # IF BIGGER THAN 1 AND BELOW TO 10 THEN SELECT "Residencial" ITEM
        elif (self.type >= 1 and self.type <= 10):
            # CORRECT THE INDEX, THE LIST INIT IN 0 THE SUBTRACT 1 OF THE CURRENT type
            convert_index = self.type - 1
            # SELECT THE ITEM
            type_list = comertial_type_list[0].find_elements_by_tag_name("option")[convert_index].click()

        # ELSE SELECT THE "Comercial" ITEM
        else:
            # HERE IS A LSIT THAT INIT IN 0 TO, BUT THE CHOOSE ITEM "type" INIT IN 11 THEN SUBTRACT "type" BY 11
            convert_index = self.type - 11
            # SELECT THE ITEM
            type_list = comertial_type_list[1].find_elements_by_tag_name("option")[convert_index].click()

        # GET THE LOCATION SEARCH FIELD
        input_location_bar = self.driver.find_element_by_id("filter-location-search-input")
        # ADD THE CHOOSE LOCATION
        input_location_bar.send_keys("Bairro "+self.local)

        time.sleep(3)

        # SEARCH
        input_location_bar.send_keys(Keys.ENTER)
        time.sleep(5)

    # GET THE MAIN APARTMENT DATA
    def getSecondPage(self, n=0):

        for district in self.neighborhood:
            self.result_list = []
            self.goToUrl(district)


            try:
                # GET THE TOTAL SEACH ITENS, THIS INFO IS ON THE TITLE
                total_itens = int(self.driver.find_element(By.CLASS_NAME, "results-summary__count").text.replace(".", ""))
            except:
                continue

            # PRE INITIALIZE VARIABLES
            pages_number = n       # NUMBER OF PAGES
            itens_by_page = 36      # A FULL PAGE HAVE A TOTAL OF 36 ITENS
            rest_itens = 0          # THE LAST PAGE CAN NOT HAVE THE 36 ITENS, EX: THE TOTAL ITENS 91, IF WE DIVIDE BY 36 WE GET
                                    # INTERE OF 2 (91//36 = 2) AND THE REST 19 (91%36 = 19).

            total_pages = total_itens // 36

            if total_pages:
                rest_itens = total_itens % 36

            # IF EXISTS ITENS BELOW OR EQUAL TO 36 ONLY ADD THE total_itens TO itens_by_page
            if total_itens <= 36:
                itens_by_page = total_itens
                pages_number = 1

            elif not n:
                pages_number = total_pages

            # ELSE CALCULATE THE NUMBER OF PAGES AND THE rest_itens
            elif pages_number > total_pages:
                pages_number = total_pages

            self.log('\n\n==================================================================================================================')
            self.log(f"{district} - Total Itens: {total_itens}  - Itens for Pages:{itens_by_page} - Rest Itens:{rest_itens}")
            self.log(f"Number Pages:{pages_number} - Total Pages:{total_pages}")


            # LOOP FOR ALL PAGES
            for i in range(total_pages):
                self.log(f"Page {i+1}\n", 2)

                # GET THE LIST OF ITENS TAG
                main_itens_tag = self.driver.find_element(By.CLASS_NAME, "results-list")
                # GET ALL ITENS
                # THE "./*" MEANS THAT I WANT ALL ELEMENTS UNDER THE ROOT ELEMENT
                itens_list = main_itens_tag.find_elements(By.XPATH, "./*")

                self.log(f"Total Itens: {len(itens_list)}", 2)

                # WALK FOR ALL THE ITENS ON THAT PAGE
                for j in range(itens_by_page):
                    try:

                        id = itens_list[j].get_attribute("id")

                        if not id:
                            item = itens_list[j].find_element(By.TAG_NAME, "div")
                            id = item.get_attribute("id")
                        else:
                            item = itens_list[j]


                        title = item.find_element(By.CLASS_NAME, "property-card__title").text       # GET THE TITLE
                        address = item.find_element(By.CLASS_NAME, "property-card__address").text   # GET THE ADDRESS
                        value = item.find_element(By.CLASS_NAME, "property-card__price").text       # GET THE VALUE

                        details= item.find_elements(By.CLASS_NAME, "property-card__detail-item")    # GET THE DETAILS TAG (area, rooms, batrooms, garage)

                        area = details[0].text
                        rooms = details[1].text
                        batrooms = details[2].text
                        garage = details[3].text

                        try:
                            amenities = item.find_element(By.CLASS_NAME, "property-card__amenities").text
                        except:
                            amenities = None

                        # GET THE URL LINK TO THE CURRENT ITEM
                        url = item.find_element(By.CLASS_NAME, "property-card__content-link").get_attribute("href")

                        # TRY TO GET THE CONDOMINIUM IF EXISTS
                        try:
                            condominium = item.find_element(By.CLASS_NAME, "property-card__price-details--condo").text
                        except:
                            condominium = None

                        # ADD TO RESULT LIST
                        # self.log(f"{id}, {title}, {address}, {value}, {condominium}, {area}, {rooms}, {batrooms}, {garage}, {url}")
                        # self.log(f"{id}, {url}, {address}, {area}, {rooms}, {batrooms}, {garage}, {amenities}, {value}, {condominium}")
                        self.log(f"{address}", 3)
                        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        self.result_list.append([id, url, address, area, rooms, batrooms, garage, amenities, value, condominium, date])

                    except Exception as e:
                        # print(f"Error : {e}")
                        continue

                    # IF THE NUMBER OF PAGES IS BIGGER THAN 1 WE NEED TO CHANGE TO THE NEXT PAGE, BUT THE "Proxima Pagina >" BUTTON NOT EXIST YET BECAUSE THE PAGE IS DYNAMICALY CREATED
                    # TO RESOLVE THIS WE NEED TO SCROLL TO THE END OF PAGE. WITH THIS BUTTON IS LOADED.
                if pages_number != (i+1) :
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                    time.sleep(1)
                    change_page_btns = self.driver.find_element(By.CLASS_NAME, "js-results-pagination")

                    try:
                        next_page_url = change_page_btns.find_elements(By.CLASS_NAME, "js-change-page")[-1].click()
                    except:
                        continue

                    time.sleep(3)

                # FINALLY IF EXISTS REST ITENS ON THE LAST PAGE GET THEN.
            if (rest_itens and (pages_number == total_pages)):
                self.log(f"Page {i}\n", 2)

                # GET THE LIST OF ITENS TAG
                main_itens_tag = self.driver.find_element(By.CLASS_NAME, "results-list")
                # GET ALL ITENS
                # THE "./*" MEANS THAT I WANT ALL ELEMENTS UNDER THE ROOT ELEMENT
                itens_list = main_itens_tag.find_elements(By.XPATH, "./*")

                self.log(f"Rest Itens: {len(itens_list)}", 2)

                for j in range(rest_itens):
                    try:

                        id = itens_list[j].get_attribute("id")

                        if not id:
                            item = itens_list[j].find_element(By.TAG_NAME, "div")
                            id = item.get_attribute("id")
                        else:
                            item = itens_list[j]


                        title = item.find_element(By.CLASS_NAME, "property-card__title").text       # GET THE TITLE
                        address = item.find_element(By.CLASS_NAME, "property-card__address").text   # GET THE ADDRESS
                        value = item.find_element(By.CLASS_NAME, "property-card__price").text       # GET THE VALUE

                        details= item.find_elements(By.CLASS_NAME, "property-card__detail-item")    # GET THE DETAILS TAG (area, rooms, batrooms, garage)

                        area = details[0].text
                        rooms = details[1].text
                        batrooms = details[2].text
                        garage = details[3].text

                        try:
                            amenities = item.find_element(By.CLASS_NAME, "property-card__amenities").text
                        except:
                            amenities = None

                        # GET THE URL LINK TO THE CURRENT ITEM
                        url = item.find_element(By.CLASS_NAME, "property-card__content-link").get_attribute("href")

                        # TRY TO GET THE CONDOMINIUM IF EXISTS
                        try:
                            condominium = item.find_element(By.CLASS_NAME, "property-card__price-details--condo").text
                        except:
                            condominium = None

                        # ADD TO RESULT LIST
                        # self.log(f"{id}, {title}, {address}, {value}, {condominium}, {area}, {rooms}, {batrooms}, {garage}, {url}")
                        # self.log(f"{id}, {url}, {address}, {area}, {rooms}, {batrooms}, {garage}, {amenities}, {value}, {condominium}")
                        self.log(f"{address}", 3)
                        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        self.result_list.append([id, url, address, area, rooms, batrooms, garage, amenities, value, condominium, date])

                    except Exception as e:
                        print(f"Error : {e}")


            self.data_manager.toCSV(self.result_list, self.columns)

    # PAGE CLOSE
    def close(self):
        self.driver.quit()

    # CODE EXECUTATION
    def run(self):
        # self.setFirstPage()
        # time.sleep(2)
        self.getSecondPage()
