from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

text = """
Agriculture plays a vital role in sustaining human life. Farmers prepare the soil, sow seeds, and nurture crops throughout the growing season. Weather conditions such as rainfall and temperature greatly influence crop yield. Modern techniques like irrigation and fertilizers have improved productivity significantly.

Sports bring people together across cultures and countries. Cricket, in particular, is one of the most popular sports globally, attracting millions of viewers during major tournaments. Events like world championships create excitement and unity among fans.

Climate change is one of the most pressing challenges facing humanity today. Rising global temperatures, melting glaciers, and extreme weather events are clear indicators of environmental imbalance. Scientists urge immediate action to reduce carbon emissions and protect ecosystems.

International conflicts can have far-reaching consequences beyond the countries directly involved. Tensions between nations such as Iran and the United States impact global trade, security, and political stability. Civilians often suffer the most during such crises.

The entertainment industry continues to evolve with new movies and creative storytelling. Bollywood produces a wide range of films every year, attracting audiences worldwide. Recently, the movie "Dhukandar" gained attention for its engaging storyline and performances.
"""

semantic_chunker=SemanticChunker(
    OpenAIEmbeddings(),
    breakpoint_threshold_type="percentile",
    breakpoint_threshold_amount=70)

docs=semantic_chunker.create_documents([text])
print(len(docs))