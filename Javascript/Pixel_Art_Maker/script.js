let button = document.querySelector('input[type="submit"]');
let form = document.querySelector('#sizePicker');
let color = document.querySelector('#colorPicker').value;


function makeGrid() {
    const canvas = document.querySelector('#pixelCanvas');

    // Creates blank canvas when page initially loads.
    canvas.innerHTML = '';

    // Get height and width values
    const height = parseInt(document.querySelector('#inputHeight').value);
    const width = parseInt(document.querySelector('#inputWidth').value);

    // Creates rows and columns. Appends rows and columns to canvas.
    for (let h = 1; h <= height; h++) {
        const row = document.createElement('tr');
        canvas.append(row);
        for (let w = 1; w <= width; w++) {
            const cell = document.createElement('td');
            row.append(cell);

            // Option to change color of each cell.
            cell.addEventListener('click', function()  {
                color = document.querySelector('#colorPicker').value;
                cell.style.backgroundColor = color;
            });
        } 
    } 
};


form.addEventListener('submit', function(event) {
    event.preventDefault();
    makeGrid()
});

