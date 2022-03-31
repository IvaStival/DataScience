// OPEN A DIALOG TO LOAD THE INPUT OR VALIDATION FILE - WORKING YET
function importData(id) {
  let input = document.createElement('input');
  input.type = 'file';
  input.onchange = _ => {
    // you can use this method to get file and perform respective operations
            let files =   Array.from(input.files);
            console.log(id);
            document.getElementById(id).value=files[0].name;
        };
  input.click();
};



// OPEN FILES, POPULATE AND CALCULATION EXECUTION
function runEnter() {

  // OPEN INPUT FILE
  var data_input;
  var data_val;

	$.ajax({
	  type: "GET",
	  url: "Inputv2.csv",
	  dataType: "text",
	  success: function(response){
      // INTERPRETATE THE CSV FILE
  		data_input = $.csv.toArrays(response, options={"separator" : ";"});
      // POPULATE
  		generateHtmlTable("items_budy_input", data_input);

      // OPEN VALIDATION FILE
      $.ajax({
        type: "GET",
        url: "Validacaov2.csv",
        dataType: "text",
        success: function(response)
        {
          // INTERPRETATE THE CSV FILE
          data_val = $.csv.toArrays(response, options={"separator" : ";"});

          // CALCULATE THE
          var calc_data = calculate(data_val, data_input);

          // POPULATE
          generateHtmlTableValidation("items_budy_validation", data_val, calc_data);
        }
      });
	  }
	});

};

// POPULATE THE TABLE INPUT WITH INPUT DATA
function generateHtmlTable(body_id, data) {

  init_val = 1;

  for (var i = init_val; i < data.length; i++) {

      var result = "<tr>"
      for(var j = 0; j < data[i].length; j++){
        result += "<td>"+data[i][j]+"</td>"
      }
      document.getElementById(body_id).innerHTML += result
  }
};

// POPULATE THE VALIDATION TABLE WITH THE VALIDATION DATA AND THE CALCULATE DATE
function generateHtmlTableValidation(body_id, data, calc_data) {

  init_val = 2

  for (var i = init_val; i < data.length; i++) {

      var result = "<tr>";
      for(var j = 0; j < data[i].length; j++){
        // THE SIZE OF INPUT DATA IS LESS THAN THE TOTAL VALIDATION DATA
        if(i < calc_data.length){
          result += "<td><p>"+data[i][j]+"</p>  <p style='color: #007F00'>" + calc_data[i-init_val][j] +"</p></td>";
        }
        else{
          result += "<td>"+data[i][j]+"</td>"
        }
      }

      // THE SIZE OF INPUT DATA IS LESS THAN THE TOTAL VALIDATION DATA
      if(i < calc_data.length){
        result += "<td><p style='color: #007F00'>" + calc_data[i-init_val][j] +"</p></td>";
      }
      document.getElementById(body_id).innerHTML += result
  }
};


function calculate(data_val, data_input){

  var val_idx = 2;
  var result = [];
  for(var i=1; i < data_input.length; i++){

    // GET THE INPUT CORRENT AND FASE VOLTAGE VALUES
    var corr_neutro = parseFloat(data_input[i][1]);
    var corr_f1 = parseFloat(data_input[i][2]);
    var corr_f2 = parseFloat(data_input[i][3]);
    var corr_f3 = parseFloat(data_input[i][4]);
    var ten_f1 = parseFloat(data_input[i][5]);
    var ten_f2 = parseFloat(data_input[i][6]);
    var ten_f3 = parseFloat(data_input[i][7]);



    var corr_total = corr_f1 + corr_f2 + corr_f3;
    console.log(corr_total)

    if(corr_neutro){
      // THE TIME VARIATION IS ABOUT 20s, IN HOURS IS EQUAL TO 0.005555
      var time = 0.0055555;

      // GET FACTOR VALUES ON VALIDATION DATASET, IT COME WITH "," DECIMAL SEPARTOR,
      // WE NEED TO REPLACE BY "."
      var factor_f1 = parseFloat(data_val[val_idx][13].replace(",", "."));
      var factor_f2 = parseFloat(data_val[val_idx][14].replace(",", "."));
      var factor_f3 = parseFloat(data_val[val_idx][15].replace(",", "."));
      var factor_total = parseFloat(data_val[val_idx][16].replace(",", "."));

      // APPARENT POTENCY CALCULATION
      // potencia_apar_fase = tensao_fase * corrent_fase
      var pot_appar_f1 = corr_f1 * ten_f1;
      var pot_appar_f2 = corr_f2 * ten_f2;
      var pot_appar_f3 = corr_f3 * ten_f3;

      // ACTIVE POTENCY CALCULATION
      // potencia_ativa_fase = potencia_fase * factor_fase
      var pot_active_f1 = pot_appar_f1 * factor_f1;
      var pot_active_f2 = pot_appar_f2 * factor_f2;
      var pot_active_f3 = pot_appar_f3 * factor_f3;

      // REACTIVE POTENCY CALCULATION
      // potencia_reativa_fase = sqrt((pot_aparent ** 2) - (pot_active ** 2))
      var pot_reactive_f1 = Math.sqrt((pot_appar_f1 ** 2) - (pot_active_f1 ** 2))
      var pot_reactive_f2 = Math.sqrt((pot_appar_f2 ** 2) - (pot_active_f2 ** 2))
      var pot_reactive_f3 = Math.sqrt((pot_appar_f3 ** 2) - (pot_active_f3 ** 2))

      // CALCULATE THE ENERGY FOR ACTIVE, REACTIVE AND APPARENT
      var energy_active_f1 = time * (pot_active_f1/1000.0);
      var energy_active_f2 = time * (pot_active_f2/1000.0);
      var energy_active_f3 = time * (pot_active_f3/1000.0);

      var energy_apar_f1 = time * (pot_appar_f1/1000.0);
      var energy_apar_f2 = time * (pot_appar_f2/1000.0);
      var energy_apar_f3 = time * (pot_appar_f3/1000.0);

      var energy_reactive_f1 = time * (pot_reactive_f1/1000.0);
      var energy_reactive_f2 = time * (pot_reactive_f2/1000.0);
      var energy_reactive_f3 = time * (pot_reactive_f3/1000.0);

      // CALCULATE THE TOTAL POTENCY AND ENERGY OF APPARENT, ACTIVE, REACTIVE
      var pot_apar_total = pot_appar_f1 + pot_appar_f2 + pot_appar_f3;
      var pot_active_total = pot_active_f1 + pot_active_f2 + pot_active_f3;
      var pot_reactive_total = pot_reactive_f1 + pot_reactive_f2 + pot_reactive_f3;
      var energy_apar_total = energy_apar_f1 + energy_apar_f2 + energy_apar_f3;
      var energy_active_total = energy_active_f1 + energy_active_f2 + energy_active_f3;
      var energy_reactive_total = energy_reactive_f1 + energy_reactive_f2 + energy_reactive_f3;

      // CALCULATE THE LINE VOLTAGE (fase_tension * sqrt(3))
      var ten_f1_f2 = ten_f1 * Math.sqrt(3);
      var ten_f2_f3 = ten_f2 * Math.sqrt(3);
      var ten_f3_f1 = ten_f3 * Math.sqrt(3);

      var dec_sep_energy = 4;
      var dec_sep_all = 2;

      result.push(["", energy_active_f1.toFixed(dec_sep_energy), energy_active_f2.toFixed(dec_sep_energy), energy_active_f3.toFixed(dec_sep_energy),
                                  energy_active_total.toFixed(dec_sep_energy), energy_apar_f1.toFixed(dec_sep_energy), energy_apar_f2.toFixed(dec_sep_energy),
                                  energy_apar_f3.toFixed(dec_sep_energy), energy_apar_total.toFixed(dec_sep_energy), energy_reactive_f1.toFixed(dec_sep_energy),
                                  energy_reactive_f2.toFixed(dec_sep_energy), energy_reactive_f3.toFixed(dec_sep_energy), energy_reactive_total.toFixed(dec_sep_energy),
                                  "", "", "", "",
                                  pot_appar_f1.toFixed(dec_sep_all), pot_appar_f2.toFixed(dec_sep_all), pot_appar_f3.toFixed(dec_sep_all), pot_apar_total.toFixed(dec_sep_all),
                                  pot_active_f1.toFixed(dec_sep_all), pot_active_f2.toFixed(dec_sep_all), pot_active_f3.toFixed(dec_sep_all), pot_active_total.toFixed(dec_sep_all),
                                  pot_reactive_f1.toFixed(dec_sep_all), pot_reactive_f2.toFixed(dec_sep_all), pot_reactive_f3.toFixed(dec_sep_all), pot_reactive_total.toFixed(dec_sep_all),
                                  "",
                                  ten_f1_f2.toFixed(dec_sep_all), ten_f2_f3.toFixed(dec_sep_all), ten_f3_f1.toFixed(dec_sep_all),
                                  "", "", "", corr_total.toFixed(dec_sep_all)]);

      val_idx += 1;
    }
  }
  return result;
}
