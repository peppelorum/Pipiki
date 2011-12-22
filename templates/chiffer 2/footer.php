		<?php get_sidebar(); ?>
	
	<!-- END .container -->
	</div>
	
	<!-- BEGIN #footer -->
	<div id="footer">	
		
		<!-- BEGIN .container -->
		<div class="container"> 
		
			<div class="span-2">
				<?php if ( !function_exists('dynamic_sidebar') || !dynamic_sidebar('First footer column') ) : ?><?php endif; ?>
			</div>
			
			<div class="span-2">
				<?php if ( !function_exists('dynamic_sidebar') || !dynamic_sidebar('Second footer column') ) : ?><?php endif; ?>
			</div>

			<div class="span-2 last" id="last_footer_col">
				<?php if ( !function_exists('dynamic_sidebar') || !dynamic_sidebar('Third footer column') ) : ?><?php endif; ?>
			</div>
			
			<div class="clear span-6">
				<hr/>
				<?php ch_credit() ?><p class="alignleft">© Copyright 2011. <?php _e("Powered by", "Chiffer"); ?> <a href="http://wordpress.org/">WordPress</a>.</p>
			</div>
			
			<p id="back-top">
				<a href="#top"><span></span><?php _e("to Top", "Chiffer"); ?></a>
			</p>
						
		<!-- END .container -->	
		</div>
		
	<!-- END #footer -->
	</div>
	
	<!-- Theme hook -->
	<?php wp_footer(); ?>

<!--END body-->
</body>

<!--END html-->
</html>