$(document).ready(function() {
    var count_page = 1
    var html_string = ''
    var showInfo = ''
    var data_get
    var max_num
    var limit = 10
    var url = ''
    $('.choice').click(function(event) {
        data_get = ""
        html_string = ''
        showInfo = ''
        event.preventDefault();
        var send_data = $(this).attr( "val" )
        console.log(send_data);
        
        if(send_data == 1){
            url = 'http://140.119.162.188:2018/cultureTW/today/json/category1.json'
        }else if(send_data == 2){
            url = 'http://140.119.162.188:2018/cultureTW/today/json/category2.json'
        }else if(send_data == 3){
            url = 'http://140.119.162.188:2018/cultureTW/today/json/category3.json'
        }else if(send_data == 4){
            url = 'http://140.119.162.188:2018/cultureTW/today/json/category4.json'
        }else if(send_data == 5){
            url = 'http://140.119.162.188:2018/cultureTW/today/json/category5.json'
        }else if(send_data == 6){
            url = 'http://140.119.162.188:2018/cultureTW/today/json/category6.json'
        }else if(send_data == 7){
            url = 'http://140.119.162.188:2018/cultureTW/today/json/category7.json'
        }else if(send_data == 8){
            url = 'http://140.119.162.188:2018/cultureTW/today/json/category8.json'
        }else if(send_data == 11){
            url = 'http://140.119.162.188:2018/cultureTW/today/json/category11.json'
        }else if(send_data == 13){
            url = 'http://140.119.162.188:2018/cultureTW/today/json/category13.json'
        }else if(send_data == 14){
            url = 'http://140.119.162.188:2018/cultureTW/today/json/category14.json'
        }else if(send_data == 15){
            url = 'http://140.119.162.188:2018/cultureTW/today/json/category15.json'
        }else if(send_data == 17){
            url = 'http://140.119.162.188:2018/cultureTW/today/json/category17.json'
        }else{
            alert('請選取適當類別！！')
        }

        $.getJSON(url, function(data) {
            data_get = data
            max_num = data.length
            if(limit <= max_num){
                for(i=0 ; i<limit ; i++){
                    
                    for(j=0 ; j<data[i].showInfo.length ; j++){
                        if(data[i].showInfo[j].location != '' || data[i].showInfo[j].locationName != '' ||data[i].showInfo[j].price != '' ||data[i].showInfo[j].time != '' || data[i].discountInfo != '' ){
                            showInfo +=
                            data[i].showInfo[j].location 
                            + "       " + 
                            data[i].showInfo[j].locationName 
                            + "       " +
                            data[i].showInfo[j].price
                            + "       " +
                            data[i].showInfo[j].time 
                            +
                            `<br>`
                        }
                    }
                    html_string += 
                    `<div class='row'>
                        <div class='col-xs-12'>
                            <h3 class='each-title'>` + 
                            data[i].title
                            + `</h3>
                        </div>
                        <div class='col-xs-7 each-content-mom'>
                            <h3>內容：</h3>
                            <p class='each-content'>` + 
                            data[i].descriptionFilterHtml
                            + `</p><h3>活動場次資訊：</h3><p class='each-content'>`
                            + showInfo + `</p><h3>優惠：</h3><p class='each-content'>` + data_get[i].discountInfo + `</p>
                        </div>
                        <div class='col-xs-5 each-detail-mom'>
                            <h3>主辦單位：</h3>
                            <p class='each-detail'>` + 
                            data[i].masterUnit 
                            + `</p><h3>售票網址：</h3><p class='each-detail'>` + 
                            data[i].webSales 
                            + `</p><h3>來源網站名稱：</h3><p class='each-detail'>` + 
                            data[i].sourceWebName 
                            + `</p>
                        </div>
                    </div>`;
                }
                $('#back').css('display','block');
                $('#back').attr('disabled','disabled');
                $('#front').css('display','block');
            }else{
                for(i=0 ; i<max_num ; i++){
                    
                    for(j=0 ; j<data[i].showInfo.length ; j++){
                        if(data[i].showInfo[j].location != '' ||data[i].showInfo[j].locationName != '' ||data[i].showInfo[j].price != '' ||data[i].showInfo[j].time != '' || data[i].discountInfo != '' ){
                            showInfo +=
                            data[i].showInfo[j].location 
                            + "       " + 
                            data[i].showInfo[j].locationName 
                            + "       " + 
                            data[i].showInfo[j].price
                            + "       " + 
                            data[i].showInfo[j].time 
                            + "       " + 
                            `<br>`
                        }
                    }
                    html_string += 
                    `<div class='row'>
                        <div class='col-xs-12'>
                            <h3 class='each-title'>` + 
                            data[i].title
                            + `</h3>
                        </div>
                        <div class='col-xs-7 each-content-mom'>
                            <h3>內容：</h3>
                            <p class='each-content'>` + 
                            data[i].descriptionFilterHtml
                            + `</p><h3>活動場次資訊：</h3><p class='each-content'>`
                            + showInfo + `</p><h3>優惠：</h3><p class='each-content'>` + data_get[i].discountInfo + `</p>
                        </div>
                        <div class='col-xs-5 each-detail-mom'>
                            <h3>主辦單位：</h3>
                            <p class='each-detail'>` + 
                            data[i].masterUnit 
                            + `</p><h3>售票網址：</h3><p class='each-detail'>` + 
                            data[i].webSales 
                            + `</p><h3>來源網站名稱：</h3><p class='each-detail'>` + 
                            data[i].sourceWebName 
                            + `</p>
                        </div>
                    </div>`;
                }
                $('#back').css('display','none');
                $('#front').css('display','none');   
            }
            document.getElementById('content').innerHTML = html_string;
            $('html, body').animate({
                scrollTop: $('#content').offset().top
            }, 2000);
        });
    })

    $('#back').click(function(event){
        event.preventDefault();
        html_string = ''
        showInfo = ''
        count_page = count_page - 1
        if(count_page == max_num/10 || limit*count_page >= max_num){
            $('#front').attr('disabled','disabled');
            $('#back').removeAttr('disabled');
        }else if(count_page == 1||  limit*count_page >= max_num ){
            $('#back').attr('disabled','disabled');
            $('#front').removeAttr('disabled');
        }else{
            $('#back').removeAttr('disabled');
            $('#front').removeAttr('disabled');
        }
        for(i=(limit*(count_page-1)) ; i<limit*count_page ; i++){    
            for(j=0 ; j<data_get[i].showInfo.length ; j++){
                if(data_get[i].showInfo[j].location != '' ||data_get[i].showInfo[j].locationName != '' ||data_get[i].showInfo[j].price != '' ||data_get[i].showInfo[j].time != '' || data_get[i].discountInfo != '' ){
                    showInfo +=
                    data_get[i].showInfo[j].location 
                    + "       " + 
                    data_get[i].showInfo[j].locationName 
                    + "       " + 
                    data_get[i].showInfo[j].price
                    + "       " + 
                    data_get[i].showInfo[j].time 
                    + "       " + 
                    `<br>`
                }
            }
            html_string += 
                `<div class='row'>
                    <div class='col-xs-12'>
                        <h3 class='each-title'>` + 
                        data_get[i].title
                        + `</h3>
                    </div>
                    <div class='col-xs-7 each-content-mom'>
                        <h3>內容：</h3>
                        <p class='each-content'>` + 
                        data_get[i].descriptionFilterHtml
                        + `</p><h3>活動場次資訊：</h3><p class='each-content'>`
                        + showInfo + `</p><h3>優惠：</h3><p class='each-content'>` + data_get[i].discountInfo + `</p>
                    </div>
                    <div class='col-xs-5 each-detail-mom'>
                        <h3>主辦單位：</h3>
                        <p class='each-detail'>` + 
                        data_get[i].masterUnit 
                        + `</p><h3>售票網址：</h3><p class='each-detail'>` + 
                        data_get[i].webSales 
                        + `</p><h3>來源網站名稱：</h3><p class='each-detail'>` + 
                        data_get[i].sourceWebName 
                        + `</p>
                    </div>
                </div>`;
        }
        document.getElementById('content').innerHTML = html_string;
        $('html, body').animate({
            scrollTop: $('#content').offset().top
        }, 2000);
    });

    $('#front').click(function(event){
        event.preventDefault();
        html_string = ''
        showInfo = ''
        count_page = count_page + 1
        if(count_page == max_num/10 || limit*count_page >= max_num){
            $('#front').attr('disabled','disabled');
            $('#back').removeAttr('disabled');
        }else if(count_page == 1||  limit*count_page >= max_num ){
            $('#back').attr('disabled','disabled');
            $('#front').removeAttr('disabled');
        }else{
            $('#back').removeAttr('disabled');
            $('#front').removeAttr('disabled');
        }
           
        for(i=(limit*(count_page-1)) ; i<limit*count_page ; i++){    
            for(j=0 ; j<data_get[i].showInfo.length ; j++){
                if(data_get[i].showInfo[j].location != '' ||data_get[i].showInfo[j].locationName != '' ||data_get[i].showInfo[j].price != '' ||data_get[i].showInfo[j].time != '' || data_get[i].discountInfo != '' ){
                    showInfo +=
                    data_get[i].showInfo[j].location 
                    + "       " + 
                    data_get[i].showInfo[j].locationName 
                    + "       " + 
                    data_get[i].showInfo[j].price
                    + "       " + 
                    data_get[i].showInfo[j].time 
                    + "       " + 
                    `<br>`
                }
            }
            html_string += 
                `<div class='row'>
                    <div class='col-xs-12'>
                        <h3 class='each-title'>` + 
                        data_get[i].title
                        + `</h3>
                    </div>
                    <div class='col-xs-7 each-content-mom'>
                        <h3>內容：</h3>
                        <p class='each-content'>` + 
                        data_get[i].descriptionFilterHtml
                        + `</p><h3>活動場次資訊：</h3><p class='each-content'>`
                        + showInfo + `</p><h3>優惠：</h3><p class='each-content'>` + data_get[i].discountInfo + `</p>
                    </div>
                    <div class='col-xs-5 each-detail-mom'>
                        <h3>主辦單位：</h3>
                        <p class='each-detail'>` + 
                        data_get[i].masterUnit 
                        + `</p><h3>售票網址：</h3><p class='each-detail'>` + 
                        data_get[i].webSales 
                        + `</p><h3>來源網站名稱：</h3><p class='each-detail'>` + 
                        data_get[i].sourceWebName 
                        + `</p>
                    </div>
                </div>`;
        }
        document.getElementById('content').innerHTML = html_string;
        $('html, body').animate({
            scrollTop: $('#content').offset().top
        }, 2000);
    });

    $("body").on("click",".each-title",function(){
        $(this).parent().parent().find(".each-content-mom").toggle('show');
        $(this).parent().parent().find(".each-detail-mom").toggle('show');
    });
})