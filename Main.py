from GrammarAnalyzer.MainParserDetection import ParserAnalyzer
from GrammarCorrection.MainParserCorrection import ParserCorrection
from Evaluation.MainEvaluater import Evaluater

# autocomplete true , false
# translate true , false
def Main(level,autocomplete,translate,text):
    grammaranalyzer = ParserAnalyzer(text)
    grammarcorrection = ParserCorrection(text)

    # print("grammar analyzer : ")
    # print(grammaranalyzer)
    # print("--"*30)

    # print("grammar correction : ")
    # print(grammarcorrection)
    # print("--"*30)

    evaluat = Evaluater(level,text, grammaranalyzer, grammarcorrection,autocomplete,translate)

    result = str(evaluat)+"###"
    for k,v in grammaranalyzer.items():
        result = result+str(k)+"#"+str(v)+"@###"

    for k,v in grammarcorrection.items():
        result = result+str(k)+"#"+str(v)+"###"

    return result


# res = Main("A1","hi,tom can play the piano.")
# # print(res)
# # print("--"*30)
# mylist = res.split("###")
# score = mylist[0]
# print("Score : "+str(score))
# mylist.pop(0)
# mylist.pop(len(mylist)-1)
# for item in mylist:
#     if str(item).endswith("@"):
#         templist = str(item).split("#")
#         print(templist[0]+" : " + templist[1]+"---------->")
#     else:
#         templist2 = str(item).split("#")
#         print(templist2[0]+" : " + templist2[1])