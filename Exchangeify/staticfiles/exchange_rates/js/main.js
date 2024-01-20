// if(appMode!="production"){console.log("main js",{appLang});console.log("main js",{baseUrl});}
// if(appMode!="development"){baseUrl=baseUrl.replace("http://","https://");}
// changeLang(appLang);var url=window.location;$('ul.nav a[href="'+url+'"]').parent().addClass("active");$("ul.nav a").filter(function(){return this.href==url;}).parent().addClass("active");function setCookie(name,value,days){if(days){var date=new Date();date.setTime(date.getTime()+days*24*60*60*1000);var expires="; expires="+date.toGMTString();}else var expires="";document.cookie=name+"="+value+expires+"; path=/";}
// function changeLang(lang){setCookie("lang",lang,1000);}
// function changeCurType(){var cur=document.getElementById("currency-select");var strCur=cur.options[cur.selectedIndex].value;setCookie("c",strCur,100);document.location.reload();}
// function changeCurCitySingle(){var cur=document.getElementById("currency-select");var strCur=cur.options[cur.selectedIndex].value;setCookie("c",strCur,100);location.href=location.href.replace(location.pathname.split("/").slice(-1)[0],strCur);}
// $("#submit_email").submit(function(e){e.preventDefault();var postData=$(this).serialize();$.ajax({url:"email_submit.php",type:"POST",data:postData,success:function(r){alert(r);},});});function getCookie(cname){var name=cname+"=";var ca=document.cookie.split(";");for(var i=0;i<ca.length;i++){var c=ca[i];while(c.charAt(0)==" ")c=c.substring(1);if(c.indexOf(name)!=-1)return c.substring(name.length,c.length);}
// return "";}
// jQuery(document).ready(function(){if(getCookie("join_tme")!=1){$("#join_tme").modal("toggle");setCookie("join_tme",1,100);}
// var cur=(function(){var cur=null;$.ajax({async:false,global:false,url:baseUrl+"/fcur/fcur2.json",dataType:"json",success:function(data){cur=data;},});return cur;})();var x=getCookie("c");var url=baseUrl+"/app_api/cur_market.json";var cursyp=(function(){var cursyp=null;$.ajax({async:false,global:false,url:url+"?"+Date.now(),dataType:"json",success:function(data){cursyp=data;},});return cursyp;})();$("#f_amount").add("#from").add("#to").add("#sell_radio").add("#buy_radio").bind("change paste keyup",function(){if($("#sell_radio").is(":checked")){cur.USDEGP=cursyp[0].ask;cur.EUREGP=cursyp[1].ask;cur.TRYEGP=cursyp[2].ask;cur.EGPEGP=cursyp[3].ask;cur.SAREGP=cursyp[4].ask;cur.JODEGP=cursyp[5].ask;cur.AEDEGP=cursyp[6].ask;cur.QAREGP=cursyp[7].ask;cur.BHDEGP=cursyp[8].ask;cur.LYDEGP=cursyp[9].ask;cur.KWDEGP=cursyp[10].ask;cur.OMREGP=cursyp[11].ask;cur.GBPEGP=cursyp[12].ask;cur.SEKEGP=cursyp[13].ask;cur.CADEGP=cursyp[14].ask;cur.NOKEGP=cursyp[15].ask;cur.DKKEGP=cursyp[16].ask;}else{cur.USDEGP=cursyp[0].bid;cur.EUREGP=cursyp[1].bid;cur.TRYEGP=cursyp[2].bid;cur.EGPEGP=cursyp[3].bid;cur.SAREGP=cursyp[4].bid;cur.JODEGP=cursyp[5].bid;cur.AEDEGP=cursyp[6].bid;cur.QAREGP=cursyp[7].bid;cur.BHDEGP=cursyp[8].bid;cur.LYDEGP=cursyp[9].bid;cur.KWDEGP=cursyp[10].bid;cur.OMREGP=cursyp[11].bid;cur.GBPEGP=cursyp[12].bid;cur.SEKEGP=cursyp[13].bid;cur.CADEGP=cursyp[14].bid;cur.NOKEGP=cursyp[15].bid;cur.DKKEGP=cursyp[16].bid;}
// from=$("#from").val();to=$("#to").val();if(from=="EGP"||to=="EGP")$(".sell_buy").fadeIn(200);else $(".sell_buy").fadeOut(200);if(cur[from+to]){rate=cur[from+to];}else if(cur[to+from]&&!cur[from+to]){rate=1/cur[to+from];}else if(from==to){rate=1;}else{rate=cur[from+to];}
// if(!rate){rate=1;}
// if(isNaN(Math.round($("#f_amount").val()*rate*1000)/1000)){$("#t_amount").val(0);}else{$("#t_amount").val(Math.round($("#f_amount").val()*rate*1000)/1000);}});$("#t_amount").add("#to").add("#from").add("#sell_radio").add("#buy_radio").bind("change paste keyup",function(){if($("#sell_radio").is(":checked")){cur.USDEGP=cursyp[0].ask;cur.EUREGP=cursyp[1].ask;cur.TRYEGP=cursyp[2].ask;cur.EGPEGP=cursyp[3].ask;cur.SAREGP=cursyp[4].ask;cur.JODEGP=cursyp[5].ask;cur.AEDEGP=cursyp[6].ask;cur.QAREGP=cursyp[7].ask;cur.BHDEGP=cursyp[8].ask;cur.LYDEGP=cursyp[9].ask;cur.KWDEGP=cursyp[10].ask;cur.OMREGP=cursyp[11].ask;cur.GBPEGP=cursyp[12].ask;cur.SEKEGP=cursyp[13].ask;cur.CADEGP=cursyp[14].ask;cur.NOKEGP=cursyp[15].ask;cur.DKKEGP=cursyp[16].ask;}else{cur.USDEGP=cursyp[0].bid;cur.EUREGP=cursyp[1].bid;cur.TRYEGP=cursyp[2].bid;cur.EGPEGP=cursyp[3].bid;cur.SAREGP=cursyp[4].bid;cur.JODEGP=cursyp[5].bid;cur.AEDEGP=cursyp[6].bid;cur.QAREGP=cursyp[7].bid;cur.BHDEGP=cursyp[8].bid;cur.LYDEGP=cursyp[9].bid;cur.KWDEGP=cursyp[10].bid;cur.OMREGP=cursyp[11].bid;cur.GBPEGP=cursyp[12].bid;cur.SEKEGP=cursyp[13].bid;cur.CADEGP=cursyp[14].bid;cur.NOKEGP=cursyp[15].bid;cur.DKKEGP=cursyp[16].bid;}
// to=$("#to").val();from=$("#from").val();if(cur[to+from]&&!cur[from+to]){rate=cur[to+from];}else if(!cur[to+from]&&cur[from+to]){rate=1/cur[from+to];}else if(from==to){rate=1;}else{rate=cur[from+to];}
// $("#f_amount").val(Math.round($("#t_amount").val()*rate*1000)/1000);});});




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


      // Get the tbody element
      var tbody = document.querySelector('.local-cur tbody');
      tbody.innerHTML = ""; // Clear existing content

      // Condition to check if the URL contains '/en/'
      var isEnglish = window.location.pathname.includes('/en/');
      var currency_numbers = isEnglish ? 15 : 7;


      // Populate the tbody with the new data
      data.slice(0, currency_numbers).forEach(currency => {
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
  console.log('Accessing cur:', cur);

})();

const fAmountInput = document.getElementById("f_amount");
const tAmountInput = document.getElementById("t_amount");



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

fromDropdown.addEventListener("change", updateCurrencyConversion);

toDropdown.addEventListener("change", updateCurrencyConversion);

sellRadio.addEventListener("change", updateCurrencyConversion);
buyRadio.addEventListener("change", updateCurrencyConversion);



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
        if (toCurrencyData.currency === "EGP") {
          console.log(toAmount)
          console.log(currency_from_value)
          const convertedToAmount = (currency_from_value / fromAmount);
          tAmountInput.value = convertedToAmount.toFixed(2);
        }
        else {
          const convertedToAmount = (fromAmount * currency_from_value) / currency_to_value;
          tAmountInput.value = convertedToAmount.toFixed(2);
        }
        
        return; // Return and terminate the function
      } else if (document.activeElement === tAmountInput) {

        
        if (fromCurrencyData.currency === "EGP") {

          const convertedFromAmount = (toAmount * currency_to_value) * toAmount;
          fAmountInput.value = convertedFromAmount.toFixed(2);

        }
        else {
          const convertedFromAmount = (toAmount * currency_to_value) / currency_from_value;
          fAmountInput.value = convertedFromAmount.toFixed(2);
        }
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

