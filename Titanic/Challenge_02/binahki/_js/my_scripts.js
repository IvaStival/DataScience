function importData(id) {
  let input = document.createElement('input');
  input.type = 'file';
  input.onchange = _ => {
    // you can use this method to get file and perform respective operations
            let files =   Array.from(input.files);
            console.log(input);
            document.getElementById(id).value=files[0].name;
        };
  input.click();
};



function runEnter() {

  var data_input;
	$.ajax({
	  type: "GET",
	  url: "Input.csv",
	  dataType: "text",
	  success: function(response)
	  {
		data_input = $.csv.toArrays(response, options={"separator" : ";"});
		generateHtmlTable("items_budy_input", data_input);
	  }
	});

  var data_val;
	$.ajax({
	  type: "GET",
	  url: "Validacaov2.csv",
	  dataType: "text",
	  success: function(response)
	  {
		data_val = $.csv.toArrays(response, options={"separator" : ";"});
		generateHtmlTable("items_budy_validation", data_val);
	  }
	});

  function generateHtmlTable(body_id, data) {

    init_val = 1
    if(body_id == "items_budy_validation"){
      init_val = 2
    }
    console.log(data[2]);
    for (var i = init_val; i < data.length; i++) {
    //     console.log(data[i][0].split(';')[1]);
        var result = "<tr>"
        for(var j = 0; j < data[i].length; j++){
          result += "<td>"+data[i][j]+"</td>"
        }
        document.getElementById(body_id).innerHTML += result
    }
  };
};

// function generateHtmlTable(body_id, data) {
//   for (var i = 1; i < data.length; i++) {
//       console.log(data[i][0].split(';')[0]);
//
//       splited_data = data[i][0].split(';');
//       // document.getElementById("items_budy").innerHTML +=  <td> Test </td> <td> Test </td> <td> Test </td>"
//       var result = "<tr>"
//       for(var j = 0; j < splited_data.length; j++){
//         result += "<td>"+splited_data[j]+"</td>"
//       }
//
//       document.getElementById("items_budy_input").innerHTML += result
//
//       // d3.select(“tbody”).insert(“tr”).html(
//       //
//       // “<td>” + [i+1] + ”</td>” +
//       // ”<td>” + (output[i][‘original_title’])+”</a>”+“</td>” +
//       // ”<td>” + (output[i][‘avg_vote’])+”</td>” +
//       // ”<td>” + (output[i][‘year’])+”</td>” +
//       // ”<td>” + (output[i][‘description’])+”</td” ) }
//   }
// };
