# gemini libのサンプルはこちら
# https://ai.google.dev/gemini-api/docs/text-generation?hl=en&lang=python#generate-text-from-text-and-image
import google.generativeai as genai

# NOTE: ここにAPIキーを入れてください．
API_KEY = ""
# モデル名
MODEL="gemini-1.5-flash"
# 要約するニュースの原稿読み上げ時間
SCRIPT_TIME = 40

def summarize_contens(description:str):
    genai.configure(api_key=API_KEY)

    model = genai.GenerativeModel(MODEL)
    question = f"""{description}
    """
    response = model.generate_content(
        f'You are a Japanese newscaster.Please summarize the given text into a manuscript that can be read in about {SCRIPT_TIME} seconds.---{question}',
        generation_config=genai.types.GenerationConfig(
            # Only one candidate for now.
            candidate_count=1,
            max_output_tokens=490,
            temperature=0.2)
    )
    return response.text