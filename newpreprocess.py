import numpy as np
import cv2
import matplotlib.pyplot as plt

def main():
	
	impath="/home/lol/Desktop/finalyr/lanedetection/Screenshot from 2019-11-26 18-14-36.png"
	#outpath="/home/lol/Desktop//grey/testeg_009.png"
	#outpath1="/home/lol/Desktop/project/noise_removal/tesetg_009.png"
	#outpath2="/home/lol/Desktop/project/equal_histogram/teestg_009.png"
	#outpath3="/home/lol/Desktop/project/morph_image/testg_009.png"
	#outpath4="/home/lol/Desktop/project/Subtraction/testg_009.png"
	#outpath5="/home/lol/Desktop/project/threshold/testg_009.png"
#	cam = cv2.VideoCapture(0)
#	s, im = cam.read() # captures image
	img=cv2.imread(impath)
	
	cv2.namedWindow("Original Image",cv2.WINDOW_NORMAL)
	cv2.imshow('Original Image',img)
	pressedkey=cv2.waitKey(0)
	img2 = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
	cv2.namedWindow("Gray Converted Image",cv2.WINDOW_NORMAL)
	cv2.imshow('Gray Converted Image',img2)
	pressedkey=cv2.waitKey(0)
	noise_removal1 = cv2.bilateralFilter(img2,9,40,40)
	noise_removal = cv2.bilateralFilter(noise_removal1,9,20,20)
	cv2.namedWindow("Noise Removed Image",cv2.WINDOW_NORMAL)
	cv2.imshow("Noise Removed Image",noise_removal)
	pressedkey=cv2.waitKey(0)
	print(type(img2))
	print((img2))
	equal_histogram = cv2.equalizeHist(noise_removal)
	kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
	morph_image=cv2.morphologyEx(equal_histogram,cv2.MORPH_OPEN,kernel,iterations=20)
	
	cv2.namedWindow("Morphological opening",cv2.WINDOW_NORMAL)
	cv2.imshow("Morphological opening",morph_image)
	pressedkey=cv2.waitKey(0)
	sub_morp_image = cv2.subtract(equal_histogram,morph_image)
	cv2.namedWindow("Subtraction image", cv2.WINDOW_NORMAL)
	
	cv2.imshow("Subtraction image", sub_morp_image)
	pressedkey=cv2.waitKey(0)

	pressedkey=cv2.waitKey(0)
	#ret,thresh_image1 = cv2.threshold(sub_morp_image,128,255,cv2.THRESH_BINARY)
	#ret,thresh_image =cv2.threshold(sub_morp_image,127,255,cv2.THRESH_BINARY)
	ret,thresh_image = cv2.threshold(sub_morp_image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	cv2.namedWindow("Image after Thresholding",cv2.WINDOW_NORMAL)
	
	cv2.imshow("Image after Thresholding",thresh_image)
	edges = cv2.Canny(thresh_image,100,200)
	cv2.imshow('canny detection',edges)
	pressedkey=cv2.waitKey(0)
	


	
	
	

	

	
	
	
	
#	cv2.imwrite(outpath3,morph_image)
#	cv2.imwrite(outpath4,sub_morp_image)
#	cv2.imwrite(outpath5,thresh_image)
#	cv2.imwrite(outpath,img2)
#	cv2.imwrite(outpath1,noise_removal)
#	cv2.imwrite(outpath2,equal_histogram)
	pressedkey=cv2.waitKey(0)
	if pressedkey==27:
		cv2.destroyAllWindows()
	
		
if __name__ == '__main__':
	main()