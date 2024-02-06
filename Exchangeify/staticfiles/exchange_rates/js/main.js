

// hide news if the the language is english
document.addEventListener("DOMContentLoaded", function() {
  let arabic_change = document.querySelector("#for_remove_this_if_news")
  if (window.location.pathname.includes("news")) {
    arabic_change.style.display = "none";
    
  }
  


})
// change from market to bank in the index  page 

function changeCurType() {
  var selectedValue = document.getElementById("currency-select").value;
  var url = `api/currencies`;

  fetch(url)
    .then(response => response.json())
    .then(data => {


      // Define the sequence of currencies
      let currencySequence = ['USD', 'EUR', 'GBP', 'SAR', 'JOB', 'AED', 'TRY', 'KWD', 'QAR', 'BHD', 'MAD', 'CAD', 'CHF', 'AUD', 'OMR'];

      // Get the tbody element
      let tbody = document.querySelector('.local-cur tbody');
      tbody.innerHTML = ""; // Clear existing content

      // Condition to check if the URL contains '/en/'
      let isEnglish = window.location.pathname.includes('/en/');
      let currency_numbers = isEnglish ? 15 : 7;

      // Filter and sort data based on the specified currency sequence
      let filteredData = data.filter(currency => currencySequence.includes(currency.currency.abbreviation));
      filteredData.sort((a, b) => currencySequence.indexOf(a.currency.abbreviation) - currencySequence.indexOf(b.currency.abbreviation));

      // Populate the tbody with the new data
      filteredData.slice(0, currency_numbers).forEach(currency => {

        var row = document.createElement("tr");

        // Conditionally choose the currency name based on language
        var currencyName = isEnglish ? currency.currency.name : currency.currency.name_ar;

        // Conditionally display fields based on selectedValue
        if (selectedValue === 'market') {
          row.innerHTML = `
              <th>
                <a href="currencies/${currency.currency.name}">
                  ${currency.currency.image ? `<img src="${currency.currency.image}" class="cur-flag" />` : '<img src="" class="cur-flag" />'}
                  <span>${currencyName}</span>
                  <span class="cur-ramz"><strong>(${currency.currency.abbreviation})</strong>:</span>
                </a>
              </th>
              <td></td>
              <td><strong>${currency.buy_market_price}</strong></td>
              <td><strong>${currency.sell_market_price}</strong></td>
              <td class="change-td">
                <span class="change-percentage" style="color: #52b55f">${currency.market_change}</span>
                <svg class="arrow up" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 12 8">
                  <path fill="none" stroke="currentcolor" stroke-linecap="round" stroke-width="2" d="m1 6 5-4 5 4"></path>
                </svg>
              </td>
            `;
        } else if (selectedValue === 'bank') {
          row.innerHTML = `
              <th>
                <a href="currencies/${currency.currency.name}">
                  ${currency.currency.image ? `<img src="${currency.currency.image}" class="cur-flag" />` : '<img src="" class="cur-flag" />'}
                  <span>${currencyName}</span>
                  <span class="cur-ramz"><strong>(${currency.currency.abbreviation})</strong>:</span>
                </a>
              </th>
              <td></td>
              <td><strong>${currency.buy_bank_price}</strong></td>
              <td><strong>${currency.sell_bank_price}</strong></td>
              <td class="change-td">
                <span class="change-percentage" style="color: #52b55f">${currency.bank_change}</span>
                <svg class="arrow up" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 12 8">
                  <path fill="none" stroke="currentcolor" stroke-linecap="round" stroke-width="2" d="m1 6 5-4 5 4"></path>
                </svg>
              </td>
            `;
        }

        // Append the row to the tbody
        tbody.appendChild(row);
      });
    })
    .catch(error => console.error("Error fetching data:", error));
}
let changeCurExist = document.getElementById("currency-select");
if (changeCurExist) {
  changeCurType()
}


document.addEventListener("DOMContentLoaded", function() {
  // languages  
  let currentPathname = window.location.pathname;
  let currentLanguage = localStorage.getItem('language');

  if (!currentLanguage) {
    currentLanguage = 'arabic';
    localStorage.setItem('language', currentLanguage);
  }

  // for news 
  if (window.location.pathname.includes("news")) {
    currentLanguage = 'arabic'
  }

  if (currentLanguage === 'english' && !currentPathname.startsWith("/en/")) {
    window.location.pathname = `/en${currentPathname}`;
  } else if (currentLanguage === 'arabic' && currentPathname.startsWith("/en/")) {
    window.location.pathname = currentPathname.replace("/en/", "/")
  }
  ///////////////
});

////////////////////


// Change language Function
function changeLanguage(event) {
  event.preventDefault(); // Prevents the default behavior of the anchor link

  let currentPathname = window.location.pathname;
  let currentLanguage = localStorage.getItem('language');

  if (!currentLanguage) {
    currentLanguage = 'arabic';
    localStorage.setItem('language', currentLanguage);
  }

  if (currentLanguage === "arabic") {
    window.location.pathname = `/en${currentPathname}`;
    localStorage.setItem('language', 'english')
  } else if (currentLanguage === "english") {
    window.location.pathname = currentPathname.replace("/en/", "/")
    localStorage.setItem('language', 'arabic')
  }


}
///////




// currency converter //
let cur;
async function fetchData() {
  if (cur) {
    console.log('Returning cached data:', cur);
    return cur;
  }

  try {
    const response = await fetch(`${window.location.origin}/api/currencies_converter`);
    const data = await response.json();

    // cur = {};
    cur = data;

    return cur;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
}

(async () => {
  cur = await fetchData();

})();

const fAmountInput = document.getElementById("f_amount");
const tAmountInput = document.getElementById("t_amount");
tAmountInput.disabled = true;



const fromDropdown = document.getElementById("from");
const toDropdown = document.getElementById("to");
const sellRadio = document.getElementById("sell_radio");
const buyRadio = document.getElementById("buy_radio");

const batchedUpdate = () => {
  const fragment = document.createDocumentFragment();
  // Perform DOM updates on the fragment
  updateCurrencyConversion();
};

fAmountInput.addEventListener("input", batchedUpdate);
tAmountInput.addEventListener("input", batchedUpdate);

fromDropdown.addEventListener("change", handleIfChange);

toDropdown.addEventListener("change", handleIfChange);

sellRadio.addEventListener("change", updateCurrencyConversion);
buyRadio.addEventListener("change", updateCurrencyConversion);

function handleIfChange() {
  fAmountInput.value = 0
  tAmountInput.value = 0
  updateCurrencyConversion()
}

// Currency Converter Function 
function updateCurrencyConversion() {
    
    // Determine whether "buy" or "sell" radio button is checked
    const sellRadio = document.getElementById("sell_radio");
    let isSellChecked = sellRadio.checked;
    isSellChecked = !isSellChecked

    const sellBuyContainer = document.querySelector(".panel-heading.sell_buy");
    if (sellBuyContainer !== null) {
      sellBuyContainer.style.display = "none";
    }
  



    // Get selected source and target currencies
    const fromDropdown = document.getElementById("from");
    const toDropdown = document.getElementById("to");
    const from = fromDropdown.value;
    const to = toDropdown.value;


    const fromAmount = parseFloat(fAmountInput.value) || 0;
    const toAmount = parseFloat(tAmountInput.value) || 0;

    // New currency information
    let newCurrency = {
      "currency": "EGP",
      "buy_market_price": (1 / (cur.find((currency) => currency.currency === "USD").buy_market_price)  ) ,
      "sell_market_price": (1 / (cur.find((currency) => currency.currency === "USD").sell_market_price)) 
    };

    // Add the new currency to the response
    cur = [...cur, newCurrency];



    const fromCurrencyData = cur.find((currency) => currency.currency === from);
    const toCurrencyData = cur.find((currency) => currency.currency === to);





    if (fromCurrencyData.currency == toCurrencyData.currency) {
        fAmountInput.value = fromAmount 
        tAmountInput.value = fAmountInput.value   
    }

    else if (fromCurrencyData && toCurrencyData) {

      // Use buy or sell market price based on radio button selection
      const currency_from_value = isSellChecked  ? fromCurrencyData.sell_market_price : fromCurrencyData.buy_market_price;
      const currency_to_value = isSellChecked ? toCurrencyData.sell_market_price : toCurrencyData.buy_market_price;



 
      
      // if the from amount or to amount is active 
      if (document.activeElement === fAmountInput) {
        if (toCurrencyData.currency === "EGP" || fromCurrencyData.currency === "EGP") {

          
          const convertedToAmount = (currency_from_value * fAmountInput.value);
          tAmountInput.value = convertedToAmount.toFixed(2);
          the_value = tAmountInput.value

        } else {

          const convertedToAmount = (fromAmount * currency_from_value) / currency_to_value;
          tAmountInput.value = convertedToAmount.toFixed(2);

        }
        
        return; // Return and terminate the function

      } else if (document.activeElement === tAmountInput) {
        console.log()
        
        
        // if (toCurrencyData.currency  === "EGP" ||  fromCurrencyData.currency === "EGP" ) {    
        //   console.log("##################")
        //   console.log(toAmount)
        //   console.log(currency_to_value)
        //   console.log(currency_from_value) 
        //   console.log((currency_from_value / 1) * toAmount)
        //   console.log("##################")
        //   const convertedFromAmount = ((currency_from_value / 1) * toAmount);
        //   fAmountInput.value = convertedFromAmount.toFixed(2);

        // } else {

        //   // const convertedFromAmount = (toAmount * currency_to_value) / currency_from_value;
        //   // fAmountInput.value = convertedFromAmount.toFixed(2);

        //   const convertedFromAmount = (toAmount * currency_to_value) ;
        //   fAmountInput.value = convertedFromAmount.toFixed(2);

          
        // }
        return; // Return and terminate the function
      }
  
      // Update both fields bidirectionally
      const convertedToAmount = (fromAmount * currency_from_value) / currency_to_value;
      tAmountInput.value = convertedToAmount.toFixed(2);
  
      const convertedFromAmount = (toAmount * currency_to_value) / currency_from_value;
      fAmountInput.value = convertedFromAmount.toFixed(2);
      console.log(fAmountInput.value);
  
      
    }
      
    }

////////////////

