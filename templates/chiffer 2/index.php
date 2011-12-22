	<?php get_header(); ?>
	
		<!-- BEGIN #content -->
		<div class="clear span-4" id="content">
		
		<?php if (is_search()) { ?>
		<h2><?php _e("Search Result for", "Chiffer"); ?> <?php /* Search Count */ $allsearch = &new WP_Query("s=$s&showposts=-1"); $key = wp_specialchars($s, 1); $count = $allsearch->post_count; _e(''); _e('<span class="search-terms">'); echo $key; _e('</span>'); _e(' &mdash; '); echo $count . ' '; _e("articles", "Chiffer"); wp_reset_query(); ?></h2>
		<hr/>
		<?php } ?>
	
		<?php while ( have_posts() ) : the_post(); // start the loop ?>
			
			<!-- BEGIN blog post -->
			<div id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
			
				<!-- BEGIN .post-header -->
	    		<div class="post-header">
	    		
	    			<h3 class="post-title"><a href="<?php the_permalink() ?>" rel="bookmark" title="<?php the_title_attribute(); ?>"><?php the_title(); ?></a></h3>
	    			
	    			<?php if (is_page()) {} else { ?>
	    			<!-- BEGIN .post-meta -->
	    			<div class="post-meta">
	    				<small>
	    					<span class="time"><?php the_time('j F, Y') ?></span> 
	    					<span class="author"><?php the_author_posts_link() ?></span> 
	    					<span class="category"><?php the_category(', '); ?></span>
	    				</small>
	    			<!-- END .post-meta -->
	    			</div>
	    			<?php } ?>
	    		
	    		<!-- END .post-header -->
	    		</div>
	    		
	    		<?php if ( has_post_thumbnail() && is_home() ) { ?> <a href="<?php the_permalink() ?>" rel="bookmark" title="<?php the_title_attribute(); ?>"><?php the_post_thumbnail('small'); // check if the post has a post thumbnail assigned to it, and if it's the index page. ?></a><?php } ?>
	    
	    		<?php if ( is_home() || is_archive() || is_search() ) : // show the_excerpt on home, archive and search pages. ?>
	    		
	    		<!-- BEGIN .post-utdrag -->
	    		<div class="post-utdrag">
	
	    			<?php the_excerpt(__('Read more →', "Chiffer"));  ?>
	    			<p><a href="<?php the_permalink() ?>" rel="bookmark" title="<?php the_title_attribute(); ?>" class="button"><?php _e("Read more →", "Chiffer"); ?></a></p>
				
	    		<!-- END .post-utdrag -->
	    		</div>
	    		
	    		<hr/>
	    		
	    		<?php else : // show the_content on all other pages ?>
	    		
	    		<!-- BEGIN .post-content -->
	    		<div class="post-content">
	    		
	    			<?php the_content(__('Read more →', "Chiffer")); ?>
	    			<?php wp_link_pages(); // for paginated posts ?>
	    		
	    		<!-- END .post-content -->
	    		</div>
	    			    		
	    		<?php endif; ?>
	    		
	    	<!-- END blog post -->	
	       	</div>
			
			<?php if (is_page()) {} else { ?>
			<?php comments_template(); // load the default comments template, remove the lines above and under this one if you want comments on your pages ?>
			<?php } ?>
			
			<?php endwhile; ?>
			
			<?php if (  $wp_query->max_num_pages > 1 ) : // if there is more than one page, show the navigation ?>
			<!-- BEGIN #nav-nedan -->
			<div id="nav-nedan">
	    		<div class="nav-fore"><?php next_posts_link( __( '← Older entries', "Chiffer" ) ); ?></div>
	    		<div class="nav-efter"><?php previous_posts_link( __( 'Newer entries →', "Chiffer" ) ); ?></div>
	    	<!-- END #nav-nedan -->
	    	</div>
	    	    	
			<?php endif; // stop the loop ?>
	
		<!-- END #content -->
		</div>
	
	<?php get_footer(); ?>