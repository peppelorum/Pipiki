<?php

/*-----------------------------------------------------------------------------------*/
/*	Google Analytics (change UA-XXXXX-X to your tracking code)
/*-----------------------------------------------------------------------------------*/

function ch_google_analytics() {
	echo '<script src="http://www.google-analytics.com/ga.js" type="text/javascript"></script>';
	echo '<script type="text/javascript">';
	echo 'var pageTracker = _gat._getTracker("UA-XXXXXXXX-X");';
	echo 'pageTracker._trackPageview();';
	echo '</script>';
}
add_action('wp_footer', 'ch_google_analytics');


/*-----------------------------------------------------------------------------------*/
/*	Make Chiffer translatable
/*-----------------------------------------------------------------------------------*/

load_theme_textdomain( 'Chiffer', TEMPLATEPATH.'/languages' );

$locale = get_locale();
$locale_file = TEMPLATEPATH."/languages/$locale.php";
if ( is_readable($locale_file) )
	require_once($locale_file);


/*-----------------------------------------------------------------------------------*/
/*	Add menu
/*-----------------------------------------------------------------------------------*/

function register_menu() {
	register_nav_menu('mainmeny', __('Main menu'));
}
add_action('init', 'register_menu');


/*-----------------------------------------------------------------------------------*/
/*	Image max width
/*-----------------------------------------------------------------------------------*/

if ( ! isset( $content_width ) ) $content_width = 630;


/*-----------------------------------------------------------------------------------*/
/*	Post thumbnails
/*-----------------------------------------------------------------------------------*/

if ( function_exists( 'add_theme_support' ) ) {
	add_theme_support( 'post-thumbnails' );
	set_post_thumbnail_size( 35, 35, true ); // This size is not used atm, but probarbly will be for custom Latest Posts widget in the future.
	add_image_size( 'medium', 300, '', true ); // Medium thumbnails - change to medium in index.php for 2 column wide thumbnails.
	add_image_size( 'small', 135, '', true ); // Small thumbnails - this size is the default size. It spans 1 column in the grid.
}


/*-----------------------------------------------------------------------------------*/
/*	Load scripts
/*-----------------------------------------------------------------------------------*/

function ch_add_stuff() {
		wp_deregister_script('jquery');
		wp_register_script('jquery', 'http://ajax.googleapis.com/ajax/libs/jquery/1.6/jquery.min.js');
		wp_register_script('selectivizr', get_template_directory_uri() . '/js/selectivizr-min.js', 'jquery');
		wp_register_script('ch_custom', get_template_directory_uri() . '/js/ch_custom.js', 'jquery', '1.0', TRUE);
		
		wp_enqueue_script('jquery');
		wp_enqueue_script('selectivizr');
		wp_enqueue_script('ch_custom');
}

add_action('wp_print_scripts', 'ch_add_stuff');


/*-----------------------------------------------------------------------------------*/
/*	Change the excerpt
/*-----------------------------------------------------------------------------------*/

function new_excerpt_more($more) {
	return ' &hellip;';
}
add_filter('excerpt_more', 'new_excerpt_more');

add_filter('excerpt_length', 'my_excerpt_length');
function my_excerpt_length($length) {
	return 60; 
}


/*-----------------------------------------------------------------------------------*/
/*	Add some widgets
/*-----------------------------------------------------------------------------------*/

function ch_widgets_init() {
	register_sidebar( array(
		'name' => 'Sidebar',
		'id' => 'sidebar_widget',
		'description' => __( 'Here are the widgets for the sidebar'),
		'before_widget' => '<div class="widget_wrap">',
		'after_widget' => '</div></div><hr class="space"/>',
		'before_title' => '<span class="h4bgr"></span><h4>',
		'after_title' => '</h4><div class="widget">',
	));
	register_sidebar( array(
		'name' => 'First footer column',
		'id' => 'footer_widget',
		'description' => __( 'First footer column.'),
		'before_widget' => '',
		'after_widget' => '',
		'before_title' => '<h4>',
		'after_title' => '</h4>',
	) );
	register_sidebar( array(
		'name' => 'Second footer column',
		'id' => 'footer_widget2',
		'description' => __( 'Second footer column.'),
		'before_widget' => '',
		'after_widget' => '',
		'before_title' => '<h4>',
		'after_title' => '</h4>',
	) );
	register_sidebar( array(
		'name' => 'Third footer column',
		'id' => 'footer_widget3',
		'description' => __( 'Third footer column.'),
		'before_widget' => '',
		'after_widget' => '',
		'before_title' => '<h4>',
		'after_title' => '</h4>',
	) );
}

add_action( 'init', 'ch_widgets_init' );


/*-----------------------------------------------------------------------------------*/
/*	Remove random junk from the head
/*-----------------------------------------------------------------------------------*/

remove_action('wp_head', 'rsd_link');
remove_action('wp_head', 'wp_generator');
remove_action('wp_head', 'feed_links', 2);
remove_action('wp_head', 'index_rel_link');
remove_action('wp_head', 'wlwmanifest_link');
remove_action('wp_head', 'feed_links_extra', 3);
remove_action('wp_head', 'start_post_rel_link', 10, 0);
remove_action('wp_head', 'parent_post_rel_link', 10, 0);
remove_action('wp_head', 'adjacent_posts_rel_link', 10, 0);


/*-----------------------------------------------------------------------------------*/
/*	Custom login logo
/*-----------------------------------------------------------------------------------*/

function ch_custom_login_logo() {
    echo '<style type="text/css">
        h1 a { background-image:url('.get_template_directory_uri().'/images/custom-login-logo.png) !important; }
    </style>';
}
function ch_wp_login_url() {
	echo home_url();
}
function ch_wp_login_title() {
	echo get_option('blogname');
}

add_action('login_head', 'ch_custom_login_logo');
add_filter('login_headerurl', 'ch_wp_login_url');
add_filter('login_headertitle', 'ch_wp_login_title');


/*-----------------------------------------------------------------------------------*/
/*	Thank you.
/*-----------------------------------------------------------------------------------*/

function ch_credit() {
	echo '<p class="alignright"><a href="http://davidpaulsson.se/chiffer-download/">Chiffer theme</a> ';
	echo _e("by", "Chiffer");
	echo ' <a href="http://davidpaulsson.se/">David Paulsson</a>.</p>';
}

?>