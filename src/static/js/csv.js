$(document).ready(function(){
 $('#load_data').click(function(){
  $.ajax({
   url:"./datos.csv",
   dataType:"text",
   success:function(data)
   {
    var employee_data = data.split(/\r?\n|\r/);
    var table_data = '<table class="table table-bordered table-striped"><tr><th>Tipo Dcto</th><th>Usuario</th><th>Link</th><th>Navegador</th><th>Fecha</th></tr>';

    for(var count = 0; count<employee_data.length; count++)
    {
     var cell_data = employee_data[count].split(";");
     table_data += '<tr>';
     for(var cell_count=0; cell_count<cell_data.length; cell_count++)
     table_data += '<td>'+cell_data[cell_count]+'</td>';
     table_data += '</tr>';
    }
    table_data += '</table>';
    $('#employee_table').html(table_data);
   }
  });
 });
});