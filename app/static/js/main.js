console.log('hello world')

$(document).ready(function(){
    var a;
    var b;
    var c;
    
    function content(){
        $('.one').click(function(){
            $('#rating').html(`rating:1`)
            a=1;
            $('.one').css("background-color", "yellow")
            console.log(a)
        })
        $('.two').click(function(){
            $('#rating').html(`rating:2`)
            a=2
        })
        $('.three').click(function(){
            $('#rating').html(`rating:3`)
            a=3
        })
        $('.four').click(function(){
            $('#rating').html(`rating:4`)
            a=4
        })
        $('.five').click(function(){
            $('#rating').html(`rating:5`)
            a=5
        })
        $('.six').click(function(){
            $('#rating').html(`rating:6`)
            a=6
        })
        $('.seven').click(function(){
            $('#rating').html(`rating:7`)
            a=7
        })
        $('.eight').click(function(){
            $('#rating').html(`rating:8`)
            a=8
        })
        $('.nine').click(function(){
            $('#rating').html(`rating:9`)
            a=9
        })
        $('.ten').click(function(){
            $('#rating').html(`rating:10`)
            a=10
        })
    }  
    
    content()

    function Design(){
        $('.creativityone').click(function(){
            $('#rating').html(`rating:1`)
            b=1;
            
        })
        $('.creativitytwo').click(function(){
            $('#rating').html(`rating:2`)
            b=2
        })
        $('.creativitythree').click(function(){
            $('#rating').html(`rating:3`)
            b=3
        })
        $('.creativityfour').click(function(){
            $('#rating').html(`rating:4`)
            b=4
        })
        $('.creativityfive').click(function(){
            $('#rating').html(`rating:5`)
            b=5
        })
        $('.creativitysix').click(function(){
            $('#rating').html(`rating:6`)
            b=6
        })
        $('.creativityseven').click(function(){
            $('#rating').html(`rating:7`)
            b=7
        })
        $('.creativityeight').click(function(){
            $('#rating').html(`rating:8`)
            b=8
        })
        $('.creativitynine').click(function(){
            $('#rating').html(`rating:9`)
            b=9
        })
        $('.creativityten').click(function(){
            $('#rating').html(`rating:10`)
            b=10
        })
        console.log(b)
    }  
    
    Design()

    function userability(){
        $('.userone').click(function(){
            $('#rating').html(`rating:1`)
            c=1;
            console.log(c)
        })
        $('.usertwo').click(function(){
            $('#rating').html(`rating:2`)
            c=2
        })
        $('.userthree').click(function(){
            $('#rating').html(`rating:3`)
            c=3
        })
        $('.userfour').click(function(){
            $('#rating').html(`rating:4`)
            c=4
        })
        $('.userfive').click(function(){
            $('#rating').html(`rating:5`)
            c=5
        })
        $('.usersix').click(function(){
            $('#rating').html(`rating:6`)
            c=6
        })
        $('.userseven').click(function(){
            $('#rating').html(`rating:7`)
            c=7
        })
        $('.usereight').click(function(){
            $('#rating').html(`rating:8`)
            c=8
        })
        $('.usernine').click(function(){
            $('#rating').html(`rating:9`)
            c=9
        })
        $('.userten').click(function(){
            $('#rating').html(`rating:10`)
            c=10
        })
    }  
    
    userability()
    total = (a+b+c)/3
    console.log(total)

})