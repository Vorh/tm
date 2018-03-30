$(document).ready(function () {

    $('#create-new-todo').submit(function (e) {
        e.preventDefault();

        var data = $('#create-new-todo').serialize();
        var gId = $('#dropdown-goals').attr('data');
        data = data + "&gId=" + gId;
        $.ajax({
            type: "POST",
            url: '/createTodo',
            data: data,
        }).done(function (resp) {
            window.location.href = '/todos';
        });

    });


    $('#create-new-goal').submit(function (e) {
        e.preventDefault();

        var data = $('#create-new-goal').serialize();
        var rewardId = $('#select-menu-rewards').attr('data');

        if (rewardId === undefined) {
            rewardId = 0;
        }
        data = data + "&rewardId=" + rewardId;
        $.ajax({
            type: "POST",
            url: '/createGoal',
            data: data,
        }).done(function (resp) {
            if (resp !== 'OK') {
                var res = JSON.parse(resp);

                if (res.captionError === true) {
                    $('#imageErrorCaption').show();
                    $('#textErrorCaption').show();
                }

                if (res.rewardError === true) {
                    $('#rewardError').show();
                }

            } else {
                window.location.href = '/goals';
            }
        });

    });

    $('#create-new-reward').submit(function (e) {
        e.preventDefault();

        var data = $('#create-new-reward').serialize();
        $.ajax({
            type: "POST",
            url: '/createReward',
            data: data,
        }).done(function (resp) {
            if (resp !== 'OK') {
                var res = JSON.parse(resp);

                if (res.captionError === true) {
                    $('#imageErrorCaption').show();
                    $('#textErrorCaption').show();
                }
                if (res.rewardError === true) {
                    $('#imageErrorReward').show();
                    $('#textErrorReward').show();
                }
            } else {
                window.location.href = '/rewards';
            }
        });

    });


    $('.btn-delete-todo').click(function () {

        var parent = $(this).closest('.item');
        var id = parent.attr('data');

        $.ajax({
            type: "POST",
            url: '/deleteTodo',
            data: {id: id}
        }).done(function (data) {
            parent.hide('slow', function () {
                parent.remove();
            });
        })
    });

    $('.btn-delete-reward').click(function () {

        var parent = $(this).closest('.item');
        var id = parent.attr('data');


        $.ajax({
            type: "POST",
            url: '/deleteReward',
            data: {id: id}
        }).done(function (data) {

            res = JSON.parse(data);
            if (res.rewardIsTied) {
                new BuildModal('The reward is tied to the goal',)
                    .addSizePx(250, 100).show();
            } else {
                parent.hide('slow', function () {
                    parent.remove();
                });
            }
        })
    });


    $('.btn-t-complete').click(function () {
        var parent = $(this).closest('.item');
        var id = parent.attr('data');

        $.ajax({
            type: "POST",
            url: '/completeTodo',
            data: {id: id}
        }).done(function (data) {
            parent.find('.todo-container').addClass('complete');
        })
    });

    $('.goal-panel').click(function () {
        var parent = $(this).closest('.item');

        $(this).find('svg').toggleClass('fa-arrow-down fa-arrow-up');

        parent.find('.goal-todo-list').slideToggle();
    });


    $('#dropdown-parent-goal').click(function () {
        $("#dropdown-goals").toggleClass("show");
    });

    $('#btn-dropdown-reward').click(function () {
        $("#dropdown-rewards").toggleClass("show");
    });


    $('#dropdown-parent-create').click(function () {
        $("#dropdown-create").toggleClass("show");
    });

    $('#dropdown-goals').on('click', 'div', function () {
        var id = $(this).attr('data');
        var caption = $(this).find("span").text();
        $('#dropdown-goals').attr('data', id);

        if (id === "0") {
            caption = "";
        }
        $('.input-dropwown').find('input').val(caption);
    });


    function BuildModal(caption) {


        m = document.createElement('div');

        $(m).addClass('modal');

        mc = document.createElement('div');
        $(mc).addClass('modal-content');

        c = document.createElement('span');
        $(c).addClass('close');
        $(c).html('&times;');


        p = document.createElement('p');
        $(p).text(caption);

        mc.appendChild(c);
        mc.appendChild(p);
        m.appendChild(mc);

        $(c).click(function () {
            m.remove();
        });


        window.onclick = function (event) {
            if (event.target == m) {
                $(m).remove();
            }
        };

        document.body.appendChild(m);


        this.addSize = function (width, height) {
            $(mc).css({'width': width, 'height': height});

            return this;
        };

        this.addSizePx = function (width, height) {
            $(mc).css({'width': width + 'px', 'height': height + 'px'});

            return this;
        };

        this.show = function () {
            $(m).show();
        };
    }

});


