import cmd

from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

class SlackBot(cmd.Cmd):
    intro = 'Welcome to the Slackbot. Type help or ? to list commands.'
    prompt = '>> '

    def __init__(self):
        model_name = "deepset/roberta-base-squad2"
        self.nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
        super().__init__()

    def do_check(self, arg):
        res = self.__answer(arg)
        prefix = arg[:res['start']]
        postfix = arg[res['end']:]
        print(prefix + '[redacted]' + postfix)

    def do_quit(self, arg):
        "Stop processing commands and exit: QUIT"
        print("Thank you for using the Slackbot")
        # NOTE: free any resources here
        return True

    def __answer(self, prompt):
        QA_input = {
            'question': 'What is my password?',
            'context': prompt
        }
        return self.nlp(QA_input)

if __name__ == "__main__":
    SlackBot().cmdloop()
