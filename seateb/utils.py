def get_instruction(task_type, task_name):
    if task_type == "STS":
        return "Retrieve semantically similar text."

    if task_type == "BitextMining":
        return "Retrieve parallel sentences."

    if task_type == "PairClassification":
        return "Retrieve semantically similar text."

    if task_type == "MultiLabelTextClassification":
        instruction_dict = {
            "Prachathai67kMultiLabelTextClassification": "Classify the given news articles into its appropriate topics",
            "TrueVoiceIntentMultiLabelTextClassification": "Given a call center query, find the corresponding intents",
            "IndoCASAMultiLabelTextClassification": "Classify the sentiment expressed in the given car reviews text from the online automobile platform",
            "IndoHoASAMultiLabelTextClassification": "Classify the sentiment expressed in the given hotel reviews text from the hotel aggregator platform",
            "VLSP2018SAHotelMultiLabelTextClassification": "Classify the sentiment expressed in the given hotel reviews text",
            "VLSP2018SARestaurantMultiLabelTextClassification": "Classify the sentiment expressed in the given restaurant reviews text",
            "DengueMultiLabelTextClassification": "Classify the given tweets into its appropriate classes",
        }

        return instruction_dict.get(task_name)

    if task_type == "QARetrieval":
        instruction_dict = {
            "ThaiTyDiQAQARetrieval": "Given a passage that is guaranteed to contain the answer, retrieve relevant passages that answer the query.",
            "IndoTyDiQAQARetrieval": "Given a passage that is guaranteed to contain the answer, retrieve relevant passages that answer the query.",
            "ThaiMIRACLQARetrieval": "Given a query and a set of documents, retrieve the documents most relevant to answering the query.",
            "IndoMIRACLQARetrieval": "Given a query and a set of documents, retrieve the documents most relevant to answering the query.",
            "ThaiXQuADQARetrieval": "Given a query and a passage, retrieve the most relevant passage that answer the query.",
            "VietnameseXQuADQARetrieval": "Given a query and a passage, retrieve the most relevant passage that answer the query.",
            "ViQuAD2_0QARetrieval": "Given a query and a passage, retrieve the most relevant passage that answer the query.",
            "VietnameseMLQAQARetrieval": "Given a query and a passage, retrieve the most relevant passage that answer the query.",
            "ThaiMLDRQARetrieval": "Given a query and a long documents, retrieve the documents most relevant to answering the query.",
            "TamilIndicQAQARetrieval": "Given a query and a passage, retrieve the most relevant passage that answer the query.",
        }
        
        return instruction_dict.get(task_name)

    if task_type == "TextClassification":
        instruction_dict = {
            "ThaiIntentTextClassification": "Given a user utterance as query, find the user intents",
            "IndoIntentTextClassification": "Given a user utterance as query, find the user intents",
            "VietnameseIntentTextClassification": "Given a user utterance as query, find the user intents",
            "TagalogIntentTextClassification": "Given a user utterance as query, find the user intents",
            "MalayIntentTextClassification": "Given a user utterance as query, find the user intents",
            "KhmerIntentTextClassification": "Given a user utterance as query, find the user intents",
            "TamilIntentTextClassification": "Given a user utterance as query, find the user intents",
            "ThaiScenarioTextClassification": "Given a user utterance as query, find the user scenarios",
            "IndoScenarioTextClassification": "Given a user utterance as query, find the user scenarios",
            "VietnameseScenarioTextClassification": "Given a user utterance as query, find the user scenarios",
            "TagalogScenarioTextClassification": "Given a user utterance as query, find the user scenarios",
            "MalayScenarioTextClassification": "Given a user utterance as query, find the user scenarios",
            "KhmerScenarioTextClassification": "Given a user utterance as query, find the user scenarios",
            "TamilScenarioTextClassification": "Given a user utterance as query, find the user scenarios",
            "WongnaiReviewsTextClassification": "Classify the given restaurant review into its appropriate rating category",
            "WisesightSentimentTextClassification": "Classify the sentiment of a given media messages as either positive, negative, or neutral",
            "GeneratedReviewsENTHTextClassification": "Classify the sentiment of a given product reviews as either accepted or rejected",
            "ThaiSentimentTextClassification": "Classify the sentiment of a given text as either positive or negative",
            "IndoSentimentTextClassification": "Classify the sentiment of a given text as either positive or negative",
            "VietnameseSentimentTextClassification": "Classify the sentiment of a given text as either positive or negative",
            "IndoSMSATextClassification": "Classify the sentiment of a given comments and reviews as either positive, negative, or neutral",
            "IndoEMOTTextClassification": "Classify the emotion expressed in the given Twitter message into one of the five emotions: anger, happy, sadness, fear, and love",
            "IndoClickbaitTextClassification": "Classify news headlines into clickbait or non-clickbait",
            "KhmerBookmebusReviewsTextClassification": "Classify the given bookmebus reviews into its appropriate rating category",
            "KhmerNewsTextClassification": "Classify news article on traffic accident into accident or non-accident",
            "TagalogProfanityTextClassification": "Classify text into profanity or non-profanity",
            "TagalogFakenewsTextClassification": "Classify fake news articles into fake news or non-fake news",
            "TagalogShopeeReviewsTextClassification": "Classify the given shopee reviews into its appropriate rating category",
            "HatespeechFilipinoTextClassification": "Classify text into hatespeech or non-hatespeech",
            "VietnameseStudentFeedbackTextClassification": "Classify students’ feedback into positive, negative, or neutral",
            "VLSP2016SentimentTextClassification": "Classify text into positive, negative, or neutral",
            "MalayNewsSentimentTextClassification": "Classify the sentiment of a given news as either positive, negative, or neutral",
            "TamilNewsTextClassification": "Classify news articles into its appropriate topic",
            "TamilmurasuNewsTextClassification": "Classify news articles into its appropriate topic",
        }
        
        return instruction_dict.get(task_name)