console.log('hello world')

$(document).ready(function(){
      for(i=1; i<=10; i++){
         var num;
        $('.one').append(`<div class="nums"> ${[i]} </div>`)
        $('.two').append(`<div class="nums"> ${[i]} </div>`)
        $('.three').append(`<div class="nums"> ${[i]} </div>`)
        
      }
    
      $('.nums').click(function(){
        for(i=1; i<=10; i++){
            var numbers = [1,2,3,4,5,6,7,8,9,10]
            var items = []
            
            $('.one').each(function(){
                         
                console.log($('.nums').value = i)
              })
        }
    
        
      })
  });
