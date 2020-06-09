library(jsonlite)


trimmedBusinessData <- stream_in(file("C:/Users/tribh/JupyterLabNotebooks/trimmedData_2.json"))
trimmedBusinessData_flat <- flatten(trimmedBusinessData)
write.csv(trimmedBusinessData, file = "C:/USA PC/Yelp_Project/yelp_data_business.csv")



trimmedReviewData <- stream_in(file("C:/Users/tribh/Downloads/trimmedReviewData.json"))
trimmedReviewData_flat <- flatten(trimmedReviewData)
write_csv(trimmedReviewData_flat, path = "C:/USA PC/Yelp_Project/yelp_data_review.csv")

