<!DOCTYPE html>

<html>
<link rel="stylesheet" href="_css/index.css">
<script src="https://code.jquery.com/jquery-1.9.1.js"></script>
<script src="_js/jquery-csv.js"></script>
<script type="text/javascript" src="_js/my_scripts.js"></script>

<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

<body>
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <h1 class=>Binahki Challenge</h1>
        <h4 class=>Enter the Input File:</h4>
        <!-- <form id="form"> -->
        <div>
        <button onclick="importData('user-input1')">Load File</button>
        <input class="form-control" id="user-input1" placeholder="Input File Path ...">
        </div>

        <h4 class=>Enter the Validation File:</h4>
        <button onclick="importData('user-input2')">Load File</button>
        <input class="form-control" id="user-input2" placeholder="Validation File Path ...">

        </form>
        <button id="button-sec" class="btn btn-secondary" onclick="runEnter()">Load Files</button>

        <div id="div_scrowll">
        <table id="table_scrowll" class="table" cellpadding="10">


        <thead>
        <tr>
          <th id="data" scope="col">Data</th>
          <th scope="col">Corrente Neutro</th>
          <th scope="col">Corrent Fase 1</th>
          <th scope="col">Corrent Fase 2</th>
          <th scope="col">Corrent Fase 3</th>
          <th scope="col">Corrent Tensão 1</th>
          <th scope="col">Corrent Tensão 2</th>
          <th scope="col">Corrent Tensão 3</th>

        </tr>
        </thead>
        </div>
        <tbody id="items_budy">
      </div>
    </div>
  </div>

</html>
