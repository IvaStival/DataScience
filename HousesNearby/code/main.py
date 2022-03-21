from WSVivaReal import WSVivaReal

bairros = ['abranches','agua-verde','ahu','alto-boqueirao','alto-da-gloria','alto-da-rua-xv','atuba','augusta','bacacheri','bairro-alto','barreirinha','batel','boa-vista','bom-retiro','boqueirao','butiatuvinha','cabral','cachoeira','cajuru','campina-do-siqueira','campo-comprido','campo-de-santana','capao-da-imbuia','capao-raso','cascatinha','centro','centro-historico','caximba','centro-civico','champagnat','cidade-industrial','cristo-rei','fanny','fazendinha','ganchinho','guabirotuba','guaira','hauer','hugo-lange','jardim-botanico','jardim-social','jardim-das-americas','juveve','lamenha-pequena','lindoia','merces','mossungue', 'ecoville','novo-mundo','orleans','parolin','pilarzinho','pinheirinho','portao','prado-velho','reboucas','riviera','santa-candida','santa-felicidade','santa-quiteria','santo-inacio','sao-braz','sao-francisco','sao-joao','sao-lourenco','sao-miguel','seminario','sitio-cercado','taboao','taruma','tatuquara','tingui','uberaba','umbara','vila-izabel','vista-alegre','xaxim']


# bairros = ['boqueirao', 'butiatuvinha', 'cabral']
cidade = "curitiba"
if __name__ == "__main__":

    web_dy = WSVivaReal(city=cidade, neighborhood=bairros, DEBUG=2, business=1)
    web_dy.initilize()
    web_dy.run()
    web_dy.close()
