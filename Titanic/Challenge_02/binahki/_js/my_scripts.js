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

  var data;
	$.ajax({
	  type: "GET",
	  url: "Input.csv",
	  dataType: "text",
	  success: function(response)
	  {
		data = $.csv.toArrays(response);
		generateHtmlTable(data);
	  }
	});

  function generateHtmlTable(data) {
    for (var i = 1; i < data.length; i++) {
        console.log(data[i][0].split(';')[0]);

        splited_data = data[i][0].split(';');
        // document.getElementById("items_budy").innerHTML +=  <td> Test </td> <td> Test </td> <td> Test </td>"
        var result = "<tr>"
        for(var j = 0; j < splited_data.length; j++){
          result += "<td>"+splited_data[j]+"</td>"
        }

        document.getElementById("items_budy").innerHTML += result

        // d3.select(“tbody”).insert(“tr”).html(
        //
        // “<td>” + [i+1] + ”</td>” +
        // ”<td>” + (output[i][‘original_title’])+”</a>”+“</td>” +
        // ”<td>” + (output[i][‘avg_vote’])+”</td>” +
        // ”<td>” + (output[i][‘year’])+”</td>” +
        // ”<td>” + (output[i][‘description’])+”</td” ) }
    }
  };
};
