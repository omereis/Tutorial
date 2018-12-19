$(document).ready(function () {

    // OUTER-LAYOUT
    var window_width = window.innerWidth;
    var backend_width = 0.25;
    $('body').layout({
        center__paneSelector:	".outer-center"
    ,	west__paneSelector:		".outer-west"
    ,	east__paneSelector:		".outer-east"
    ,	west__size:				125
    ,	east__size:				125
    ,	spacing_open:			8  // ALL panes
    ,	spacing_closed:			12 // ALL panes
    //,	north__spacing_open:	0
    //,	south__spacing_open:	0
    ,	north__maxSize:			200
    ,	south__maxSize:			200

        // MIDDLE-LAYOUT (child of outer-center-pane)
    ,	center__childOptions: {
            center__paneSelector:	".middle-center"
        ,	west__paneSelector:		".middle-west"
        ,	east__paneSelector:		".middle-east"
        ,	west__size:				100
        ,	east__size:				window_width * backend_width
        ,	spacing_open:			8  // ALL panes
        ,	spacing_closed:			12 // ALL panes

            // INNER-LAYOUT (child of middle-center-pane)
        ,	center__childOptions: {
                center__paneSelector:	".inner-center"
            ,	west__paneSelector:		".inner-west"
            ,	east__paneSelector:		".inner-east"
            ,	west__size:				75
            ,	east__size:				(window_width * (1 - backend_width)) / 2
            ,	spacing_open:			8  // ALL panes
            ,	spacing_closed:			8  // ALL panes
            ,	west__spacing_closed:	12
            ,	east__spacing_closed:	12
            }
        }
    });

});
