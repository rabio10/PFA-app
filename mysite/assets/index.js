const ctx = document.getElementById('myChart');
const firstChart = document.getElementById('first-Chart');

// envoyer GET request pour récupérer les données de prévision total
document.addEventListener('DOMContentLoaded', (event) => {
  fetch('/prevision_total_json/')
      .then(response => response.json())
      .then(data => {
          console.log(data);  // Log the entire data for debugging
          const totals = data.map(item => item.total);
          console.log(totals);  // Log the totals array for debugging
          // Now you have the array of totals from the 2nd column
      })
      .catch(error => console.error('Error fetching data:', error));
});


//on va prendre les données de prévision depuis la base de données
const dataPrevision = [15, 14, 18, 40, 22, 17, 22, 24, 24, 31, 41, 56, 48, 53, 61, 64, 67, 65, 73, 88, 80, 81, 80, 78, 78, 77, 82, 79, 64, 64, 63, 58, 63, 58, 61, 55, 45, 43, 37, 26, 34, 30, 29, 29, 30, 23, 20, 24, 24, 22, 19, 17];
new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52'],
    datasets: [{
      label: '# de demande prevu',
      data: dataPrevision,
      borderWidth: 1
    }]
  },
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});

//après on va prendre ces données depuis la base de données à partir d'un fichier Json ou API ?
const dataPreviousSemestre = [41,37,32,20,27,26,20,17,19,26,20,16,16];

new Chart(previousData, {
type: 'line',
data: {
  labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
  datasets: [{
    label: 'Qte demande',
    data: dataPreviousSemestre ,
    borderWidth: 1
  }]
},
options: {
  scales: {
    y: {
      beginAtZero: true
    }
  }
}
});

//après on va prendre ces données depuis la base de données à partir d'un fichier Json ou API ?
const dataNextSemestre = [15, 14, 18, 40, 22, 17, 22, 24, 24, 31, 41, 56, 48];

new Chart(nextData, {
type: 'line',
data: {
  labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
  datasets: [{
    label: 'Qte demande',
    data: dataNextSemestre ,
    borderWidth: 1
  }]
},
options: {
  scales: {
    y: {
      beginAtZero: true
    }
  }
}
});

//----------------------------------------------
//polar chart

//après on va prendre ces données par calcule et depuis base de données
const dataPerTrimestre = [372, 945, 772, 327];

new Chart(polarChart,{
  type: 'polarArea',
  data: {
    labels: [
      'Trimestre 1',
      'Trimestre 2',
      'Trimestre 3',
      'Trimestre 4',
    ],
    datasets: [{
      label: 'Hausse par trimestre',
      data: dataPerTrimestre,
      backgroundColor: [
        'rgb(255, 99, 132)',
        'rgb(75, 192, 192)',
        'rgb(255, 205, 86)',
        'rgb(201, 203, 207)'
      ]
    }]
  },
  options: {}
});
