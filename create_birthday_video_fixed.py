#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Birthday Invitation Video Generator for Avyaansh Jain's 1st Birthday
Run this in Google Colab or local environment with required libraries installed
"""

import os
from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def create_birthday_video():
    """
    Creates a birthday invitation video using the provided photos
    """
    
    # Video settings
    WIDTH, HEIGHT = 1920, 1080  # HD resolution
    FPS = 24
    DURATION_PER_SLIDE = 4  # seconds
    
    def create_text_clip(text, duration, fontsize=60, color='white', position='center'):
        """Create a text clip with specified properties"""
        return TextClip(text, 
                       fontsize=fontsize, 
                       color=color, 
                       font='Arial-Bold',
                       stroke_color='black',
                       stroke_width=2).set_duration(duration).set_position(position)
    
    def create_background_clip(color, duration):
        """Create a colored background clip"""
        background = ColorClip(size=(WIDTH, HEIGHT), color=color, duration=duration)
        return background
    
    # Create slides
    clips = []
    
    # Slide 1: Welcome
    bg1 = create_background_clip((135, 206, 235), DURATION_PER_SLIDE)  # Sky blue
    text1 = create_text_clip("You're Invited!", DURATION_PER_SLIDE, fontsize=80, color='white')
    slide1 = CompositeVideoClip([bg1, text1])
    clips.append(slide1)
    
    # Slide 2: To Celebrate
    bg2 = create_background_clip((255, 192, 203), DURATION_PER_SLIDE)  # Pink
    text2 = create_text_clip("To celebrate", DURATION_PER_SLIDE, fontsize=70, color='darkblue')
    slide2 = CompositeVideoClip([bg2, text2])
    clips.append(slide2)
    
    # Slide 3: Avyaansh's Name
    bg3 = create_background_clip((255, 255, 224), DURATION_PER_SLIDE)  # Light yellow
    text3_1 = create_text_clip("Avyaansh Jain's", DURATION_PER_SLIDE, fontsize=75, color='darkgreen', position=('center', 400))
    text3_2 = create_text_clip("1st Birthday!", DURATION_PER_SLIDE, fontsize=90, color='red', position=('center', 500))
    
    # Add big "1" with decorations
    big_one = create_text_clip("1", DURATION_PER_SLIDE, fontsize=200, color='gold', position=('center', 200))
    slide3 = CompositeVideoClip([bg3, big_one, text3_1, text3_2])
    clips.append(slide3)
    
    # Slide 4: Event Details
    bg4 = create_background_clip((240, 248, 255), DURATION_PER_SLIDE)  # Alice blue
    details_text = """Date: 22 September
Time: 5 PM
Venue: Deepali Hotel"""
    text4 = create_text_clip(details_text, DURATION_PER_SLIDE, fontsize=60, color='darkblue')
    slide4 = CompositeVideoClip([bg4, text4])
    clips.append(slide4)
    
    # Slide 5: Join Us
    bg5 = create_background_clip((255, 182, 193), DURATION_PER_SLIDE)  # Light pink
    join_text = """Join us for fun, laughter, and cake
as we celebrate Avyaansh turning ONE!"""
    text5 = create_text_clip(join_text, DURATION_PER_SLIDE, fontsize=50, color='darkred')
    slide5 = CompositeVideoClip([bg5, text5])
    clips.append(slide5)
    
    # Slide 6: Can't wait to see you
    bg6 = create_background_clip((152, 251, 152), DURATION_PER_SLIDE)  # Pale green
    text6 = create_text_clip("Can't wait to see you there!", DURATION_PER_SLIDE, fontsize=70, color='darkgreen')
    slide6 = CompositeVideoClip([bg6, text6])
    clips.append(slide6)
    
    # Concatenate all clips
    final_video = concatenate_videoclips(clips, method="compose")
    
    return final_video

def create_video_with_photos():
    """
    Enhanced version that includes actual photos
    Place your photos in the same directory and update the file paths
    """
    
    # Photo file paths (update these to match your actual file names)
    photo_paths = [
        "0M3A3188.JPG",
        "0M3A3228.JPG", 
        "0M3A3313.JPG",
        "0M3A3316.JPG"
    ]
    
    clips = []
    DURATION_PER_SLIDE = 4
    
    for i, photo_path in enumerate(photo_paths):
        if os.path.exists(photo_path):
            # Load and resize photo
            img_clip = ImageClip(photo_path, duration=DURATION_PER_SLIDE)
            img_clip = img_clip.resize(height=800).set_position('center')
            
            # Create background
            bg = ColorClip(size=(1920, 1080), color=(255, 182, 193), duration=DURATION_PER_SLIDE)
            
            # Add text overlay based on slide number
            if i == 0:
                text = TextClip("You're Invited!", fontsize=80, color='white', stroke_color='black', stroke_width=3)
                text = text.set_duration(DURATION_PER_SLIDE).set_position(('center', 100))
            elif i == 1:
                text = TextClip("Avyaansh Jain's 1st Birthday!", fontsize=70, color='gold', stroke_color='darkblue', stroke_width=3)
                text = text.set_duration(DURATION_PER_SLIDE).set_position(('center', 900))
            elif i == 2:
                text = TextClip("Date: 22 September | Time: 5 PM", fontsize=60, color='white', stroke_color='black', stroke_width=2)
                text = text.set_duration(DURATION_PER_SLIDE).set_position(('center', 100))
            else:
                text = TextClip("Venue: Deepali Hotel", fontsize=60, color='white', stroke_color='black', stroke_width=2)
                text = text.set_duration(DURATION_PER_SLIDE).set_position(('center', 900))
            
            # Compose the slide
            slide = CompositeVideoClip([bg, img_clip, text])
            clips.append(slide)
    
    # Add final message slide
    final_bg = ColorClip(size=(1920, 1080), color=(152, 251, 152), duration=DURATION_PER_SLIDE)
    final_text = TextClip("Can't wait to see you there!", fontsize=80, color='darkgreen', stroke_color='white', stroke_width=3)
    final_text = final_text.set_duration(DURATION_PER_SLIDE).set_position('center')
    final_slide = CompositeVideoClip([final_bg, final_text])
    clips.append(final_slide)
    
    return concatenate_videoclips(clips, method="compose")

def main():
    """
    Main function to create and export the birthday video
    """
    
    print("Creating Avyaansh's Birthday Invitation Video...")
    
    try:
        # Choose which version to create
        # Option 1: Text-only version (works without photos)
        video = create_birthday_video()
        
        # Option 2: Version with photos (uncomment if you have photos ready)
        # video = create_video_with_photos()
        
        # Export the video
        output_path = "avyaansh_birthday_invitation.mp4"
        print(f"Exporting video to: {output_path}")
        
        video.write_videofile(
            output_path,
            fps=24,
            codec='libx264',
            audio_codec='aac',
            temp_audiofile='temp-audio.m4a',
            remove_temp=True
        )
        
        print("Video created successfully!")
        print(f"Saved as: {output_path}")
        print(f"Duration: {video.duration:.2f} seconds")
        
    except Exception as e:
        print(f"Error creating video: {str(e)}")
        print("Make sure you have installed required libraries:")
        print("   pip install moviepy pillow numpy")

if __name__ == "__main__":
    main()


# INSTALLATION INSTRUCTIONS:
"""
1. Install required libraries:
   pip install moviepy pillow numpy

2. For Google Colab:
   !pip install moviepy pillow numpy

3. Run the script:
   python create_birthday_video_fixed.py

4. The video will be saved as 'avyaansh_birthday_invitation.mp4'
"""
