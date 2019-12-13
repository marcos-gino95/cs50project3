document.addEventListener('DOMContentLoaded', () => {


  document.querySelectorAll('#show').forEach(span => {
    span.onclick = () => {
      var divrad = document.querySelectorAll('.toppi');
      var radios = document.querySelectorAll('#topp');
      var buttons = document.querySelectorAll('#show')

      for (var i = 0; i < divrad.length; i++) {
        if (span.dataset.allow == divrad[i].dataset.allow) {
          if (divrad[i].style.display == "block" ) {
            divrad[i].style.display = 'None';
            for (var j = 0; j < radios.length; j++)
              {radios[j].checked = false;
              radios[j].disabled = false;
              for (var l = 0; l < buttons.length; l++)
                  buttons[l].disabled = false;}
          } else {
            divrad[i].style.display = 'block';
            for (var k = 0; k < radios.length; k++)
              {radios[k].checked = false;
              radios[k].disabled = false;
              for (var l = 0; l < buttons.length; l++)
                if (l != i)
                  buttons[l].disabled = true;}
          }
        }
      }

    };
  });
  document.querySelectorAll('#topp').forEach(radio => {
    radio.onclick = () => {
      var radios = document.querySelectorAll('#topp');
      if (document.querySelectorAll('input[type="checkbox"]:checked').length == radio.dataset.allow) {
          for (var i = 0; i < radios.length; i++)
            if (radios[i].checked == false)
              radios[i].disabled = true;
      }else {
        for (var i = 0; i < radios.length; i++)
          if (radios[i].checked == false)
            radios[i].disabled = false;
      }
    }
  });
  var items = document.querySelectorAll('.item');
  var total = 0;
  for (var i = 0; i < items.length; i++) {
    total = total + parseFloat(items[i].innerHTML);
  }
  document.querySelector('.total').innerHTML =  total.toFixed(2);
});
