const btn_click = document.getElementById('button');

btn_click.addEventListener('click', function(){

    Swal.fire("Este Modulo Admin  organiza la información y facilita el análisis de Graficos Interactivos.");
});



drawChart();
    
async function drawChart() {
const dataPoints = await getData();   

const data = {
   labels: dataPoints.labels2,
   datasets: [{
     label: dataPoints.UsuariosPorAño,
     data: dataPoints.Anio,
     backgroundColor: [
       'rgba(255, 26, 104, 0.2)',
       'rgba(54, 162, 235, 0.2)',
       'rgba(255, 206, 86, 0.2)',
       'rgba(75, 192, 192, 0.2)',
       'rgba(153, 102, 255, 0.2)',
       'rgba(255, 159, 64, 0.2)',
       'rgba(0, 0, 0, 0.2)'
     ],
     borderColor: [
       'rgba(255, 26, 104, 1)',
       'rgba(54, 162, 235, 1)',
       'rgba(255, 206, 86, 1)',
       'rgba(75, 192, 192, 1)',
       'rgba(153, 102, 255, 1)',
       'rgba(255, 159, 64, 1)',
       'rgba(0, 0, 0, 1)'
     ],
     borderWidth: 1
   }]
 };

 // config 
 const config = {
   type: 'line',
   data,
   options: {
     scales: {
       y: {
         beginAtZero: true
       }
     }
   }
 };

 // render init block
 const myChart = new Chart(
   document.getElementById('grafico'),
   config
 );

 // Gráfico de barras 

};
 
 async function getData() {
   const labels = [];
   const labels2 = [];
   const labels3 = [];
    
     const response = await fetch('/static/uploads/signup.csv');
     const data=await response.text();
     console.log(data);


       
     const table = data.split('\n').slice(1);

     table.forEach(row => {
       const column = row.split(',');

       const fecha = column[3];
       const nombre = column[4];

       labels.push(fecha);
       labels2.push(nombre);



     });

     const UsuariosPorAño = "UsuariosPorAño";
     const Anio = [2021,2022,2023,2024];

     return {labels,labels2,UsuariosPorAño,Anio}
 };


