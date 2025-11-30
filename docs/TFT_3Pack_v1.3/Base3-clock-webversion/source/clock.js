/***********************************************************************************
 * Created by the NostraDomus development team.                                    *
 *                                                                                 *
 * Check https://github.com/nostradomus/Base3-clock for more details               *
 ***********************************************************************************/

/* Function to convert a decimal value into an array of "colors".
   The array contains only 4 elements, as the highest possible value is 59 minutes.*/
  function convertToTernaryColors(decimal) {
    var ternaryColors = ["whitesmoke", "whitesmoke", "whitesmoke", "whitesmoke"];
    var div;
    var rem;
    for (i = 0; i < 4; i++) {
        div = Math.floor(decimal/Math.pow(3, 3-i));
        rem = decimal % Math.pow(3, 3-i);
        switch(div) {
            case 1:
                ternaryColors[i] = "yellowgreen";
                break;
            case 2:
                ternaryColors[i] = "orangered";
                break;
          }
        decimal = rem;
      }
    return ternaryColors
  }

/* function to update the clock digits                                             */
  function refreshClock() {
      /* get a reference to the table containing the digits                        */
      var x = document.getElementById("timetable").getElementsByTagName("td");

      /* get the current timestamp from the local machine                          */
      var date = new Date;
      var seconds = date.getSeconds();
      var minutes = date.getMinutes();
      var hour = date.getHours();

      /* convert hours/minutes/seconds to their ternary representation             */
      var ternaryHour = convertToTernaryColors(hour);
      var ternaryMinutes = convertToTernaryColors(minutes);
      var ternarySeconds = convertToTernaryColors(seconds);

      /* update the coloured squares in the table                                  */
      for (i = 0; i < 4; i++) {
        x[i].style.backgroundColor = ternaryHour[i];
        }
      for (i = 0; i < 4; i++) {
        x[i+4].style.backgroundColor = ternaryMinutes[i];
        }
      for (i = 0; i < 4; i++) {
        x[i+8].style.backgroundColor = ternarySeconds[i];
        }
  }
