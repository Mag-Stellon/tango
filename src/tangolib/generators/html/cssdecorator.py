class CSSGeneratorDecorator(DocumentGenerator):

    def __init__(self, delegateHTML):
        self.delegate = delegateHTML
        pass

class CSSCommandGeneratorDecorator(CommandGenerator):
    pass

class CSSEnvironmentGeneratorDecorator(EnvironmentGenerator):
    pass

class CSSSectionGeneratorDecorator(SectionGenerator):
    pass

class CSSTextGeneratorDecorator(TextGenerator):
    pass

class CSSPreformatedGeneratorDecorator(PreformatedGenerator):
    pass

class CSSSpacesGeneratorDecorator(SpacesGenerator):
    pass

class CSSNewlinesGeneratorDecorator(NewlinesGenerator):
    pass
