$(document).ready(function () {
    const object = {}
    var button_state = true
    $('#result_teams').css('display', 'none')
    $('#retry').css('display', 'none')

    $('body').on('click','#start_simulation',function () {
        const json = JSON.stringify(object);

            $.post("/api/home/simulation/", {data: json}, function (data) {
                console.log(data)
                if (data.result[0] === 0) {

                    $('.away').css('display', 'none')
                    $('#ocult_input_local').css('display', 'none')
                    $('#result_teams').text(data.team).css('display', 'block')

                } else if (data.result[0] === 1) {
                    $('.local').css('display', 'none')
                    $('#ocult_input_away').css('display', 'none')
                    $('#result_teams').text(data.team).css('display', 'block')

                } else {
                    $('.local').css('display', 'none')
                    $('.away').css('display', 'none')
                    $('#result_teams').text(data.team).css('display', 'block')
                }

                $('#start_simulation').css('display', 'none')
                $('#retry').css('display', 'block')


            }).fail(function (xhr, textStatus, errorThrown) {
                alert(xhr.responseText);
            });


    });

    $('body').on('click', '#retry',function () {

            $('.local').css('display', 'block')
            $('.away').css('display', 'block')
            $('#result_teams').css('display', 'none')
            $('#start_simulation').css('display', 'block')
            $('#retry').css('display', 'none')

    })

    $('#local_team').change(function () {
        var id_local = $(this).val()
        object['local_team'] = id_local;

        $.get("/api/home/team/"+parseInt(id_local)+"/",{},function (data){
            console.log(data)

            $('#local_img').attr('src',data['result']['logo'])
            $('#local_img_stats').attr('src',data['result']['logo'])
            $('#local_name_stats').text(data['result']['name'])
            $('#local_corners').text(data['result']['corner'])
            $('#local_corners_p').text((parseFloat(data['result']['corner'])/38).toFixed(2))
            $('#local_fouls').text(data['result']['fouls_committed'])
            $('#local_fouls_p').text(((parseFloat(data['result']['fouls_committed'])/38).toFixed(2)))
            $('#local_ycard').text(data['result']['yellow_card'])
            $('#local_ycard_p').text(((parseFloat(data['result']['yellow_card'])/38).toFixed(2)))
            $('#local_rcard').text(data['result']['red_card'])
            $('#local_rcard_p').text(((parseFloat(data['result']['red_card'])/38).toFixed(2)))
            $('#local_shoots').text(data['result']['shots'])
            $('#local_shoots_p').text(((parseFloat(data['result']['shots'])/38).toFixed(2)))
            $('#local_dshoots').text(data['result']['shots_on_target'])
            $('#local_dshoots_p').text(((parseFloat(data['result']['yellow_card'])/38).toFixed(2)))

        });
    });

    $('#away_team').change(function () {
        var id_local = $(this).val()
        object['away_team'] = id_local;

        $.get("/api/home/team/"+parseInt(id_local)+"/",{},function (data){
            console.log(data['result']['logo'])

            $('#away_img').attr('src',data['result']['logo'])
            $('#away_img_stats').attr('src',data['result']['logo'])
            $('#away_name_stats').text(data['result']['name'])
            $('#away_corners').text(data['result']['corner'])
            $('#away_corners_p').text((parseFloat(data['result']['corner'])/38).toFixed(2))
            $('#away_fouls').text(data['result']['fouls_committed'])
            $('#away_fouls_p').text(((parseFloat(data['result']['fouls_committed'])/38).toFixed(2)))
            $('#away_ycard').text(data['result']['yellow_card'])
            $('#away_ycard_p').text(((parseFloat(data['result']['yellow_card'])/38).toFixed(2)))
            $('#away_rcard').text(data['result']['red_card'])
            $('#away_rcard_p').text(((parseFloat(data['result']['red_card'])/38).toFixed(2)))
            $('#away_shoots').text(data['result']['shots'])
            $('#away_shoots_p').text(((parseFloat(data['result']['shots'])/38).toFixed(2)))
            $('#away_dshoots').text(data['result']['shots_on_target'])
            $('#away_dshoots_p').text(((parseFloat(data['result']['yellow_card'])/38).toFixed(2)))

        });
    });
});