import cmd

from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

class SlackBot(cmd.Cmd):
    intro = 'Welcome to the Slackbot. Type help or ? to list commands.'

    def do_quit(self, arg):
        "Stop processing commands and exit: QUIT"
        print("Thank you for using the Slackbot")
        # NOTE: free any resources here
        return True

    def __answer(self):
        model_name = "deepset/roberta-base-squad2"

        nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
        QA_input = {
            'question': 'Why is model conversion important?',
            'context': 'The option to convert models between FARM and transformers gives freedom to the user and lets people easily switch between frameworks.'
        }
        res = nlp(QA_input)

        return res['answer']

if __name__ == "__main__":
    SlackBot().cmdloop()
