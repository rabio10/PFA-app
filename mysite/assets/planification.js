console.log('plaaaaaaaan'); // Add this line
/*
//script pour ajouter un depot
document.getElementById('addDepotBtn').addEventListener('click', function() {
    const depotForm = document.createElement('div');
    depotForm.className = 'depot mt-4';
    depotForm.innerHTML = `
      <h4>Ajouter Dépôt</h4>
      <div class="form-group">
        <label for="depotName">Nom Dépôt</label>
        <input type="text" class="form-control" placeholder="Nom Dépôt">
      </div>
      <div class="form-group">
        <label for="depotCity">Ville</label>
        <input type="text" class="form-control" placeholder="Ville">
      </div>
      <div class="form-group">
        <label for="depotStock">Stock Dispo</label>
        <input type="number" class="form-control" placeholder="Stock Dispo">
      </div>
      <div class="form-group">
        <label for="historicalFile">Fichier Historique</label>
        <input type="file" class="form-control-file">
      </div>
    `;
    document.getElementById('depots').appendChild(depotForm);
  });
  */
  
  //script pour afficher les données du trimestre depuis la base de données selon le choix de l'utilisateur
  // dans la page de planification 
  const trimesterSelect = document.getElementById('trimesterSelect');
  if (trimesterSelect){
    trimesterSelect.addEventListener('change', function(event) {
    event.preventDefault();
    console.log('Trimester changed'); // Debug
    const selectedTrimester = event.target.value;
    updateTable(selectedTrimester);
  
  });
}
  const data = [
    // Sample data for 52 weeks
    { week: 1, prevision: 100, stock: 50, command: 20 },
    { week: 2, prevision: 110, stock: 55, command: 25 },
    { week: 3, prevision: 120, stock: 60, command: 30 },
    { week: 4, prevision: 130, stock: 65, command: 35 },
    { week: 5, prevision: 140, stock: 70, command: 40 },
    { week: 6, prevision: 150, stock: 75, command: 45 },
    { week: 7, prevision: 160, stock: 80, command: 50 },
    { week: 8, prevision: 170, stock: 85, command: 55 },
    { week: 9, prevision: 180, stock: 90, command: 60 },
    { week: 10, prevision: 190, stock: 95, command: 65 },
    { week: 11, prevision: 200, stock: 100, command: 70 },
    { week: 12, prevision: 210, stock: 105, command: 75 },
    { week: 13, prevision: 220, stock: 110, command: 80 },
    { week: 14, prevision: 230, stock: 115, command: 85 },
    { week: 15, prevision: 240, stock: 120, command: 90 },
    { week: 16, prevision: 250, stock: 125, command: 95 },
    { week: 17, prevision: 260, stock: 130, command: 100 },
    { week: 18, prevision: 270, stock: 135, command: 105 },
    { week: 19, prevision: 280, stock: 140, command: 110 },
    { week: 20, prevision: 290, stock: 145, command: 115 },
    { week: 21, prevision: 300, stock: 150, command: 120 },
    { week: 22, prevision: 310, stock: 155, command: 125 },
    { week: 23, prevision: 320, stock: 160, command: 130 },
    { week: 24, prevision: 330, stock: 165, command: 135 },
    { week: 25, prevision: 340, stock: 170, command: 140 },
    { week: 26, prevision: 350, stock: 175, command: 145 },
    { week: 27, prevision: 360, stock: 180, command: 150 },
    { week: 28, prevision: 370, stock: 185, command: 155 },
    { week: 29, prevision: 380, stock: 190, command: 160 },
    { week: 30, prevision: 390, stock: 195, command: 165 },
    { week: 31, prevision: 400, stock: 200, command: 170 },
    { week: 32, prevision: 410, stock: 205, command: 175 },
    { week: 33, prevision: 420, stock: 210, command: 180 },
    { week: 34, prevision: 430, stock: 215, command: 185 },
    { week: 35, prevision: 440, stock: 220, command: 190 },
    { week: 36, prevision: 450, stock: 225, command: 195 },
    { week: 37, prevision: 460, stock: 230, command: 200 },
    { week: 38, prevision: 470, stock: 235, command: 205 },
    { week: 39, prevision: 480, stock: 240, command: 210 },
    { week: 40, prevision: 490, stock: 245, command: 215 },
    { week: 41, prevision: 500, stock: 250, command: 220 },
    { week: 42, prevision: 510, stock: 255, command: 225 },
    { week: 43, prevision: 520, stock: 260, command: 230 },
    { week: 44, prevision: 530, stock: 265, command: 235 },
    { week: 45, prevision: 540, stock: 270, command: 240 },
    { week: 46, prevision: 550, stock: 275, command: 245 },
    { week: 47, prevision: 560, stock: 280, command: 250 },
    { week: 48, prevision: 570, stock: 285, command: 255 },
    { week: 49, prevision: 580, stock: 290, command: 260 },
    { week: 50, prevision: 590, stock: 295, command: 265 },
    { week: 51, prevision: 600, stock: 300, command: 270 },
    { week: 52, prevision: 610, stock: 305, command: 275 },
    // Add data for all 52 weeks...
  ];
  
  function updateTable(trimester) {
    const tableBody = document.getElementById('tableBody');
    if (!tableBody) return; // Stop if the table body is not found
    tableBody.innerHTML = ''; // Clear existing table data
    const startWeek = (trimester - 1) * 13 + 1;
    const endWeek = startWeek + 12;
  
    const filteredData = data.filter(d => d.week >= startWeek && d.week <= endWeek);
    filteredData.forEach(d => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td>${d.week}</td>
        <td>${d.prevision}</td>
        <td>${d.stock}</td>
        <td>${d.command}</td>
      `;
      tableBody.appendChild(row);
    });
  }
  
  // Initialize table with the first trimester data
  updateTable(1);

  //--------------------------------------------------------------------------------
  // script de population des données de la table de prevision
  const trimesterSelectPrev = document.getElementById('trimesterSelectPrev');
  if (trimesterSelectPrev){
    trimesterSelectPrev.addEventListener('change', function(event) {
    event.preventDefault();
    console.log('Trimester changed'); // Debug
    const selectedTrimesterPrev = event.target.value;
    updateTablePrev(selectedTrimesterPrev);
  
  });
}
  
  /*const dataPrev = [
    // Sample data for 52 weeks
    { week: 1, prevision: 100},
    { week: 2, prevision: 110},
    { week: 3, prevision: 120},
    { week: 4, prevision: 130},
    { week: 5, prevision: 140},
    { week: 6, prevision: 150},
    { week: 7, prevision: 160},
    { week: 8, prevision: 170},
    { week: 9, prevision: 180},
    { week: 10, prevision: 190},
    { week: 11, prevision: 200},
    { week: 12, prevision: 210},
    { week: 13, prevision: 220},
    { week: 14, prevision: 230},
    { week: 15, prevision: 240},
    { week: 16, prevision: 250},
    { week: 17, prevision: 260 },
    { week: 18, prevision: 270 },
    { week: 19, prevision: 280 },
    { week: 20, prevision: 290 },
    { week: 21, prevision: 300 },
    { week: 22, prevision: 310 },
    { week: 23, prevision: 320 },
    { week: 24, prevision: 330 },
    { week: 25, prevision: 340 },
    { week: 26, prevision: 350 },
    { week: 27, prevision: 360 },
    { week: 28, prevision: 370 },
    { week: 29, prevision: 380 },
    { week: 30, prevision: 390 },
    { week: 31, prevision: 400 },
    { week: 32, prevision: 410 },
    { week: 33, prevision: 420 },
    { week: 34, prevision: 430 },
    { week: 35, prevision: 440 },
    { week: 36, prevision: 450 },
    { week: 37, prevision: 460 },
    { week: 38, prevision: 470 },
    { week: 39, prevision: 480 },
    { week: 40, prevision: 490 },
    { week: 41, prevision: 500 },
    { week: 42, prevision: 510 },
    { week: 43, prevision: 520 },
    { week: 44, prevision: 530 },
    { week: 45, prevision: 540 },
    { week: 46, prevision: 550 },
    { week: 47, prevision: 560 },
    { week: 48, prevision: 570 },
    { week: 49, prevision: 580 },
    { week: 50, prevision: 590 },
    { week: 51, prevision: 600 },
    { week: 52, prevision: 610 },
    // Add data for all 52 weeks...
  ];*/
  const dataPrev = window.dicPrevisionTotal;
  console.log(dataPrev);
  
  function updateTablePrev(trimester) {
    const tableBody = document.getElementById('tablePrev');
    if (!tableBody) return; // Stop if the table body is not found
    tableBody.innerHTML = ''; // Clear existing table data
    const startWeek = (trimester - 1) * 13 + 1;
    const endWeek = startWeek + 12;
  
    const filteredData = dataPrev.filter(d => d.semaine >= startWeek && d.semaine <= endWeek);
    filteredData.forEach(d => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td>${d.semaine}</td>
        <td>${d.prevision}</td>
      `;
      tableBody.appendChild(row);
    });
  }
  
  // Initialize table with the first trimester data
  updateTablePrev(1);

  //--------------------------------------------------------------------------------
  // find the biggest value in the prevision data
  const maxPrevisionData = dataPrev.reduce((max, item) => item.prevision > max.prevision ? item : max, dataPrev[0]);

  // maxPrevisionData now contains the data item with the highest prevision
  const maxPrevision = maxPrevisionData.prevision;
  const semaineOfMaxPrevision = maxPrevisionData.semaine;  
  //put it in html 
  document.getElementById('card').textContent = maxPrevision;
  document.getElementById('semaineMax').textContent = `En Semaine ${semaineOfMaxPrevision}`;
