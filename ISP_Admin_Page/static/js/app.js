console.log("We are live")

$( ".client_sterge" ).on("click", function() {
    var client_id = $(this).attr('id')
    var returncode = confirm("Esti sigur ca vrei sa stergi clientul?")
    
    console.log("id ul este " + client_id)
    console.log('aaa')
    if (returncode) {
        $.ajax({
            type: "GET",
            url: '/clienti/sterge/' + client_id,
            dataType: "json",
            success: function(data, textStatus) {
                if (data) {
                    window.location.href = '/clienti/1';
                } else {
                    console.log("OK")
                }
            }
        })
    }
  })