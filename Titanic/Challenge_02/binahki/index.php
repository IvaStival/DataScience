<!DOCTYPE html>

<html>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<link rel="stylesheet" href="_css/index.css">
<script src="https://code.jquery.com/jquery-1.9.1.js"></script>
<script src="_js/jquery-csv.js"></script>
<script type="text/javascript" src="_js/my_scripts.js"></script>



<body>
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <h1 class=>Binahki Challenge</h1>

        <form id="form">
          <h4 class=>Enter the Input File:</h4>
          <div id="input_labels">
              <button onclick="importData('user-input1')">Load File</button>
              <input class="form-control" id="user-input1" placeholder="Input File Path ...">
          </div>

          <h4 class=>Enter the Validation File:</h4>
          <div id="input_labels">
            <button onclick="importData('user-input2')">Load File</button>
            <input class="form-control" id="user-input2" placeholder="Validation File Path ...">
          </div>

        </form>
        <button id="button-sec" class="btn btn-secondary" onclick="runEnter()">Load Files</button>

        <div id="div_scrowll_input">
          <table id="table_scrowll" class="table" cellpadding="10">

            <thead>
              <tr>
                  <th id="data" scope="col">Data</th>
                  <th scope="col">Corrente Neutro</th>
                  <th scope="col">Corrent Fase 1</th>
                  <th scope="col">Corrent Fase 2</th>
                  <th scope="col">Corrent Fase 3</th>
                  <th scope="col">Tensão Fase 1</th>
                  <th scope="col">Tensão Fase 2</th>
                  <th scope="col">Tensão Fase 3</th>
              </tr>
            </thead>


        <tbody id="items_budy_input"></tbody>
        </table>
        </div>

        <div id="div_scrowll_validation">
          <table id="table_scrowll" class="table" cellpadding="10">
              <thead>
                  <tr>
                    <th id="data" scope="col">Data</th>
                    <th scope="col">energia ativa f1</th>
                    <th scope="col">energia ativa f2</th>
                    <th scope="col">energia ativa f3</th>
                    <th scope="col">energia ativa total</th>
                    <th scope="col">energia aparente f1</th>
                    <th scope="col">energia aparente f2</th>
                    <th scope="col">energia aparente f3</th>
                    <th scope="col">energia aparente total</th>
                    <th scope="col">energia reativa f2</th>
                    <th scope="col">energia reativa f1</th>
                    <th scope="col">energia reativa f3</th>
                    <th scope="col">energia reativa total</th>
                    <th scope="col">fator potencia f1</th>
                    <th scope="col">fator potencia f2</th>
                    <th scope="col">fator potencia f3</th>
                    <th scope="col">Fator Potencia Total</th>
                    <th scope="col">potencia aparente f1</th>
                    <th scope="col">potencia aparente f2</th>
                    <th scope="col">potencia aparente f3</th>
                    <th scope="col">potencia aparente total</th>
                    <th scope="col">potencia ativa f1</th>
                    <th scope="col">potencia ativa f2</th>
                    <th scope="col">potencia ativa f3</th>
                    <th scope="col">potencia ativa total</th>
                    <th scope="col">potencia reativa f1</th>
                    <th scope="col">potencia reativa f2</th>
                    <th scope="col">potencia reativa f3</th>
                    <th scope="col">potencia reativa total</th>
                    <th scope="col">temperatura</th>
                    <th scope="col">tensao f1_f2</th>
                    <th scope="col">tensao f2_f3</th>
                    <th scope="col">tensao f3_f1</th>
                    <th scope="col">angulo tensao f1</th>
                    <th scope="col">angulo tensao f2</th>
                    <th scope="col">angulo tensao f3</th>
                    <th scope="col">Corrent Total</th>
                  </tr>
              </thead>

          <tbody id="items_budy_validation">
          </table>
          </div>


      </div>
    </div>
  </div>
  <div id="name"> By Iva Reinaldo Stival </div>

</html>
