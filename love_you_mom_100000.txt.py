# Define a heartfelt Shayari for Mom
shayari = """🌸 माँ की ममता का कोई मोल नहीं,  
उसके बिना ये जीवन अनमोल नहीं।  
दुआओं में जिसकी ताकत अपार,  
वो है मेरी माँ, मेरा संसार! ❤️"""

# Open a file and write the Shayari + 100,000 "LOVE YOU" messages
with open("love_you_mom_100000.txt", "w", encoding="utf-8") as file:
    file.write(shayari + "\n\n")  # Write Shayari first
    file.write(("LOVE YOU 💖\n" * 100000))  # Write "LOVE YOU" 100,000 times

print("✅ 100,000 'LOVE YOU' messages with a heartfelt Shayari for Mom saved successfully! 💕")

