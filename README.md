# Weather
This is a project about Analysis of the weather which decides you should go outside or not.

Firstly,I use Scrapy crawl some dates about weather including in temperature,weather conditions which indicate sunny，raining，or others，wind and its strength all chinese cities.Besides，the type of files downloading containing txt，csv，json.

And then，I deal with  csv file once upon time in order to accumulate for after.You know,machine learing need comfortable date to train，or you will not get correct result what you wants.In this project， I process date with normalized those string data which need to be numbers first of all.

Now， We owm many date about  hundreds of thousands.So, we can start  training.

Here,I use Classification tree and SVM model train.We can obverse the output result between both of them and thinking which is better if result is good enough.
