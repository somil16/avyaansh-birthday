#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Final Birthday Invitation Video Generator
This script creates a video that mimics the two-panel design of 'final_invitation.html'.
"""

import os
from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont

def create_final_video():
    """
    Generates the final birthday invitation video.
    """
    WIDTH, HEIGHT = 1200, 700
    FPS = 24
    PHOTO_DURATION = 3  # seconds per photo

    # --- Create the static info panel (right side) ---
    info_panel_bg = ColorClip(size=(500, HEIGHT), color=(255, 255, 255))
    
    # You may need to adjust font paths based on your system
    try:
        title_font = ImageFont.truetype("Arial", 50)
        subtitle_font = ImageFont.truetype("Arial", 20)
        details_font = ImageFont.truetype("Arial", 18)
        footer_font = ImageFont.truetype("Arial", 18)
    except IOError:
        print("Default fonts not found. Using generic font.")
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        details_font = ImageFont.load_default()
        footer_font = ImageFont.load_default()

    # Create a PIL image to draw text on
    img = Image.new('RGB', (500, HEIGHT), color = (255, 255, 255))
    d = ImageDraw.Draw(img)

    # Draw text
    d.text((250, 150), "Our little star\nis turning one!", font=title_font, fill=(142, 68, 173), anchor="mm", align="center")
    d.text((250, 250), "Join us to celebrate Avyaansh Jain's 1st Birthday", font=subtitle_font, fill=(52, 73, 94), anchor="mm", align="center")
    
    d.text((250, 350), "📅 Date: 22 September", font=details_font, fill=(52, 73, 94), anchor="mm")
    d.text((250, 390), "🕔 Time: 5:00 PM", font=details_font, fill=(52, 73, 94), anchor="mm")
    d.text((250, 430), "🏨 Venue: Deepali Hotel", font=details_font, fill=(52, 73, 94), anchor="mm")

    d.text((250, 550), "Cake, giggles, and fun await!", font=footer_font, fill=(52, 152, 219), anchor="mm")

    # Convert PIL image to MoviePy clip
    info_panel_clip = ImageClip(img).set_duration(PHOTO_DURATION * 5) # 5 photos

    # --- Create the animated photo panel (left side) ---
    photo_paths = [
        "0M3A3363.JPG",
        "0M3A3188.JPG",
        "0M3A3313.JPG",
        "0M3A3316.JPG",
        "0M3A3355.JPG"
    ]
    
    photo_clips = []
    for path in photo_paths:
        if os.path.exists(path):
            clip = (ImageClip(path)
                    .set_duration(PHOTO_DURATION)
                    .resize(width=700)
                    .set_position("center"))
            photo_clips.append(clip)
        else:
            print(f"Warning: Photo not found at {path}. Skipping.")

    if not photo_clips:
        print("Error: No photos found. Cannot create video.")
        return

    # Concatenate the photo clips to play one after another
    animated_photos = concatenate_videoclips(photo_clips, method="compose").fadein(1).fadeout(1)

    # --- Combine the two panels ---
    final_video = clips_array([
        [animated_photos, info_panel_clip]
    ])

    # Add background music (optional)
    # audio = AudioFileClip("path/to/your/music.mp3").set_duration(final_video.duration)
    # final_video = final_video.set_audio(audio)

    # Export the video
    output_path = "birthday_invitation_video.mp4"
    print(f"Exporting video to: {output_path}")
    final_video.write_videofile(output_path, fps=FPS)
    print("✅ Video created successfully!")

if __name__ == "__main__":
    create_final_video()
