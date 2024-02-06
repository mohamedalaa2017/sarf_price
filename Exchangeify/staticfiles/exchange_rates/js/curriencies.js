let currencies_data;

// get currencies prices and put it in currencies_data 
//variable but we have to run this function first if we are in block
async function fetchCurrenciesData() {
    if (currencies_data) {
        return currencies_data;
    }

    try {
        let url = window.location.origin + `/api/currencies`;
        const response = await fetch(url);
        const data = await response.json();

        currencies_data = data;

        return currencies_data;
    } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
    }
}

// to put currencies in innerHTML of tbody
function displayCurrencies(data) {
    let tableBody = document.getElementById("currencies_tbody_data");

    // Clear the table body
    tableBody.innerHTML = "";

    // Loop through the data array
    data.forEach(function (currency) {
        // Create a new table row
        let newRow = document.createElement("tr");

        // Add data-currency-id attribute to identify each row
        newRow.setAttribute("data-currency-id", currency.id);

        // Create the first table cell with the currency information
        let currencyCell = document.createElement("th");
        let currencyLink = document.createElement("a");
        currencyLink.href = window.location.origin + `/currencies/${currency.currency.name}`;

        // Add the currency image if available
        if (currency.currency.image) {
            let currencyImage = document.createElement("img");
            currencyImage.src = currency.currency.image;
            currencyImage.classList.add("cur-flag");
            currencyLink.appendChild(currencyImage);
        }

        // Add the currency name based on language code
        let currencyName = document.createElement("span");
        if (language_type_now === 'arabic') {
            currencyName.textContent = currency.currency.name_ar;
        } else {
            currencyName.textContent = currency.currency.name;
        }
        currencyLink.appendChild(currencyName);

        // Add the currency abbreviation
        let currencyAbbreviation = document.createElement("span");
        currencyAbbreviation.classList.add("cur-ramz");
        currencyAbbreviation.innerHTML = "<strong>(" + currency.currency.abbreviation + ")</strong>";
        currencyLink.appendChild(currencyAbbreviation);

        currencyCell.appendChild(currencyLink);
        newRow.appendChild(currencyCell);

        // Add empty cells for the second and third columns
        newRow.innerHTML += "<td></td><td><strong>" + currency.buy_market_price + "</strong></td>";

        // Add the fourth column with sell market price
        let sellMarketPriceCell = document.createElement("td");
        sellMarketPriceCell.innerHTML = "<strong>" + currency.sell_market_price + "</strong>";
        newRow.appendChild(sellMarketPriceCell);

        // Add the fifth column with market change and arrow
        let marketChangeCell = document.createElement("td");
        marketChangeCell.classList.add("change-td");

        let changePercentage = document.createElement("span");
        changePercentage.classList.add("change-percentage");
        changePercentage.style.color = "#52b55f";
        changePercentage.textContent = currency.market_change;
        marketChangeCell.appendChild(changePercentage);

        let arrowSvg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        arrowSvg.classList.add("arrow", "up");
        arrowSvg.setAttribute("xmlns", "http://www.w3.org/2000/svg");
        arrowSvg.setAttribute("viewBox", "0 0 12 8");

        let arrowPath = document.createElementNS("http://www.w3.org/2000/svg", "path");
        arrowPath.setAttribute("fill", "none");
        arrowPath.setAttribute("stroke", "currentcolor");
        arrowPath.setAttribute("stroke-linecap", "round");
        arrowPath.setAttribute("stroke-width", "2");
        arrowPath.setAttribute("d", "m1 6 5-4 5 4");

        arrowSvg.appendChild(arrowPath);
        marketChangeCell.appendChild(arrowSvg);

        newRow.appendChild(marketChangeCell);

        // Append the new row to the table body
        tableBody.appendChild(newRow);
    });
}



// display currencies based on language
async function getAllCurrencies(language_type) {
    
    await fetchCurrenciesData(); // Wait for data to be fetched


    // Rest of your code
    const CurrencyOrder = ['USD', 'EUR', 'GBP', 'SAR', 'JOB', 'AED', 'TRY', 'KWD', 'QAR', 'BHD', 'MAD', 'CAD', 'CHF', 'AUD', 'OMR'];
    let tableBody = document.getElementById("currencies_tbody_data");
    
    // Sort the data array based on the desired currency order
    currencies_data.sort((a, b) => {
        const indexA = CurrencyOrder.indexOf(a.currency.abbreviation);
        const indexB = CurrencyOrder.indexOf(b.currency.abbreviation);

        // If both currencies are in the desired order, sort based on their positions
        if (indexA !== -1 && indexB !== -1) {
            return indexA - indexB;
        }

        // If only one currency is in the desired order, prioritize it
        if (indexA !== -1) {
            return -1;
        }
        if (indexB !== -1) {
            return 1;
        }

        // If neither currency is in the desired order, maintain the original order
        return 0;
    });

    displayCurrencies(currencies_data)
           
}








// search 
document.addEventListener("DOMContentLoaded",  function() {
    let tableBody = document.getElementById("currencies_tbody_data");
    let searchInput = document.getElementById("curSearch");
  

    if (searchInput) {
      searchInput.addEventListener("input", function () {
        
        let searchTerm = searchInput.value.toLowerCase(); 

        if (searchInput.value.length < 1 ) {
            getAllCurrencies(language_type_now)

        } else {
            tableBody.innerHTML = '';

            let filteredCurrencies = currencies_data.filter(currency => {
                const name = (language_type_now === 'arabic') ? currency.currency.name_ar : currency.currency.name;
                const includesSearchTerm = name.toLowerCase().includes(searchTerm) || currency.currency.abbreviation.toLowerCase().includes(searchTerm);
                return includesSearchTerm;
            });
            // Display the filtered currencies
            displayCurrencies(filteredCurrencies);
        
        }
        
      });
    } else {
      console.error("Element with ID 'curSearch' not found.");
    }
  });
  


