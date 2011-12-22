<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:og="http://opengraphprotocol.org/schema/"
      xmlns:fb="http://www.facebook.com/2008/fbml" <?php language_attributes(); ?>>

<!-- BEGIN head -->	      
<head>

	<!-- 
	
		Chiffer theme by @davidpaulsson, http://davidpaulsson.se, http://wpkod.se
		
	-->
	
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
	<meta charset="<?php bloginfo( 'charset' ); ?>" />
	
	<!-- Facebook meta -->
	<?php if (have_posts()):while(have_posts()):the_post();endwhile;endif; ?>
	<meta property="fb:app_id" content="YOUR_APP_ID" />
	<meta property="fb:admins" content="YOUR_FACEBOOK_ID" />
	<meta property="og:site_name" content="<?php bloginfo('name'); ?>" />
	<?php if (is_single()) { ?>
	<meta property="og:url" content="<?php the_permalink() ?>"/>
	<meta property="og:title" content="<?php single_post_title(''); ?>" />
	<meta property="og:description" content="<?php echo strip_tags(get_the_excerpt($post->ID)); ?>" />
	<meta property="og:type" content="article" />
	<meta property="og:image" content="<?php echo wp_get_attachment_thumb_url( get_post_thumbnail_id( $post->ID ) ) ?>" />
	<?php } else { ?>
	<meta property="og:description" content="<?php bloginfo('description'); ?>" />
	<meta property="og:type" content="website" />
	<meta property="og:image" content="<?php bloginfo('template_url') ?>/images/YOUR_LOGO.png" />
	<?php } ?>
	
	<!-- Title -->
	<title><?php wp_title(''); ?></title>
	
	<!-- Favicon & iPhone/Android -->
	<link rel="shortcut icon" href="<?php bloginfo('template_url'); ?>/images/favicon.ico">
	<link rel="apple-touch-icon" href="<?php bloginfo('template_url'); ?>/images/apple-touch-icon.png">	
	
	<!-- Load Google fonts -->
	<link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Droid+Serif|Pacifico" type="text/css" />
	
	<!-- CSS -->
	<link rel="stylesheet" href="<?php bloginfo('template_url'); ?>/css/screen.css" type="text/css" media="screen, projection" />
	<link rel="stylesheet" href="<?php bloginfo('template_url'); ?>/css/print.css" type="text/css" media="print" />
	<!--[if lt IE 8]><link rel="stylesheet" href="<?php bloginfo('template_url'); ?>/css/ie.css" type="text/css" media="screen, projection"/><![endif]-->
	<link rel="stylesheet" href="<?php bloginfo( 'stylesheet_url' ); ?>" />
	
	<link rel="pingback" href="<?php bloginfo( 'pingback_url' ); ?>" />
	
	<!-- Theme hook -->
	<?php wp_head(); ?>
	
</head><!-- END head -->	

<!-- BEGIN body -->
<body <?php body_class(); ?>>

	<!-- BEGIN .container -->
	<div class="container">
	
		<!-- BEGIN #menu -->
		<div class="span-6 last" id="menu">                
			<?php /*
			Change 'Home' to 'Blog' or whatever you want your home link to be named */
			wp_page_menu( array( 'show_home' => 'Home', 'sort_column' => 'menu_order' ) ); ?>
		<!-- END #menu -->
		</div>
	
		<!-- BEGIN #header -->
		<div class="clear span-4" id="header">
			<h1><a href="<?php bloginfo('url'); ?>" title="<?php bloginfo('name'); ?>"><?php bloginfo( 'name' ); ?></a></h1>
			<p><?php bloginfo( 'description' ); ?></p>
		<!-- END #header -->
		</div>
		
		<!-- BEGIN #search -->
		<div class="span-2 last" id="search">
			<form method="get" id="searchform" action="<?php bloginfo('url'); ?>/">
				<input type="text" value="<?php the_search_query(); ?>" name="s" id="s" class="searchfield" />
				<input type="submit" id="searchsubmit" value="search" class="searchbutton"/>
			</form>
		<!-- END #search -->
		</div>