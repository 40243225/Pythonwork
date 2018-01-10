# -*- coding: utf8 -*-
# coding: utf8
import jieba
import jieba.analyse

jieba.load_userdict("./dict/userdict.txt")
jieba.analyse.set_stop_words("./dict/stop_words.txt")
jieba.analyse.set_idf_path("./dict/idf.txt");
content="網路流傳蓮花產品可以抗癌，這是真的嗎"
#content="網路流傳蓮花專門克制癌細胞，可以讓腫瘤細胞變良性，有效對抗癌症，這是真的嗎？ (1)      由於國人健康意識的提升，對於食品保健相關議題更加重視，所以有關食品問題的傳言也越來越多，但多數是誇大或未經證實的內容，常常引起許多民眾的恐慌。關於坊間流傳「蓮花可使腫瘤變良性而抗癌」的訊息，內容沒有相關的資訊來源，而且也沒有相關科學論述依據，對於這種沒有根據的傳言，應該抱持小心謹慎的態度，不要隨便輕易相信。 (2)      食藥署提醒，民眾應該保持均衡飲食，養成健康的生活習慣，適當運動並維持理想體重，建立正確的營養攝取觀念，才能維持身體健康。如有身體不適，應適時就醫並遵醫囑治療，勿聽信偏方而延誤就醫時機。"
tags = jieba.analyse.extract_tags(content, topK=5)
print(",".join(tags))