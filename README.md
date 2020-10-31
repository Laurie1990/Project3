# Project 3- Machine Learning

## About this project

This project aims to use machine learning to help identify households where children are most at risk of leaving education and participating in the labour market. In many developing countries, this is a significant issue which prevents educational attainment for children, generally leading to lower lifetime incomes, and impedes the accumulation of human capital- undermining further economic development in these countries.

This project utilizes a datasource collected by the [SMERU Research Institute](https://smeru.or.id/en/about), which conducted a study on the effects of Uncoditional Cash Transfers (UCT's) on child labour within households between 2005 and 2006 in Indonesia. The original purpose of the data collection was to facilitate a rigorous policy impact evaluation, comparing households that received the UCT (the treated) to those that did not (the untreated group). Using various techniques, researchers have sought to identify the Average Treatment Effect (measured in differences between treated and untreated groups) of and attribute causality to government policy interventions.

Rather than perform a policy impact evalutation, in this project, we propose to use machine learning techniques to try and classify households most at risk of child labour participation. We will do this by confining our analysis to the untreated group of households. Using the initial household data collected via survey in 2005, we will train our model to predict and classify households most likely to have child labour, which was recorded in a follow-up survey in 2006. The benefit of this is that it allows for more effective targeting of groups for government policy intervention, delivering a greater social and economic benefit for the use of public funds.

An app demonstrating this machine learning model can be found here: https://child-labour-predict.herokuapp.com/


## Technologies used
* Python/Pandas
* MatplotLib
* Flask
* Sklearn
* Javascript
* Heroku

- - -

# Process
* 1. In notebooks, extract data from stata file (.dta format), export as csv to data.
* 2. In notebooks, read csv from #1 clean and preprocess data, EDA. Export cleaned data as csv to data.
* 3. In notebooks, read cleaned data and explore different modelling approaches. Select a final model.
* 4. In model, create model.py that replicates our final model from #3.
* 5. In model, save a trained version of our model as model.joblib which can be loaded at command.
* 6. In general repository, create app.py to build a web application.
* 7. In templates, create an html page for input which can be passed back to our trained model in #5.
* 8. In static/js, create app.js which takes and formats inputs from #7 upon form submission, passes to stored model and returns a prediction.
* 9. In general repository, create Procfile, link to Hero and host app.



- - -

## Helpful Links

* [Unconditional Cash Transfers](https://en.wikipedia.org/wiki/Unconditional_cash_transfer)

* [A study relating to this UCT program](https://www.business.uwa.edu.au/__data/assets/pdf_file/0004/2053084/Bazzi,-Sumarto,-Suryahadi-3ie-Report-March-2012.pdf)

- - -
## Acknowledgements
The team of Uzair Khan, Laurie Walker and Tahsin Rahman would like to acknowledge and thank our instructor Ryan, as well as our TA's Nick and Mish.
The html file and app.js borrow heavily from a class demonstration given by our instructor Ryan.

- - -
## Copyright
A portion of this dataset was supplied to the one of the authors, as part of their study in developmental economics at the Australian National University. 
This data is not intended for commercial use. All data has been anonymised.
