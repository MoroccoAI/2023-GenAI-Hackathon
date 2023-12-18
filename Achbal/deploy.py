import os.path
import os
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space 
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
from llama_index import (
    Document,
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)
path = "المقاولة والأعمال\الصفقات العمومية"

# Side bar contents
with st.sidebar:
    st.title('الذكاء الاصطناعي أشبال')
    st.markdown('''
    ## معلومات عنا:
    هذا التطبيق هو تواصل مع الذكاء الاصطناعي أشبال مدعومة ب (LLM) تم بناؤه باستخدام:
    - [Streamlit](https://streamlit.io/)
    - [OpenAI](https://platform.openai.com/docs/models) LLM Model
    - [Idarati dataset](https://www.idarati.ma/)
    ''')
    add_vertical_space(5)
    st.write('تم إنشاؤه من قبل فريق أشبال')
st.title('تواصل مع الذكاء الاصطناعي أشبال')



if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant",  "content": "اسألني سؤالاً حول مكتبة مستندات مفتوحة المصدر Idarati !"}
    ]



@st.cache_resource(show_spinner=False)
def load_index():
    with st.spinner(text="جاري تحميل  مستندات اداراتي  انتظر قليلاً! قد يستغرق هذا الأمر من 1 إلى 2 دقيقة."):
        if not os.path.exists("./storage"):
            # load the documents and create the index
            # documents = SimpleDirectoryReader(path).load_data()
            documents = [Document(id_='c44713bb-32e4-4aaa-976b-4d9b4cd9273e', embedding=None, metadata={'file_path': 'D:\\MoroccanAI\\Hackathon1\\Streamlit\\المقاولة والأعمال\\الصفقات العمومية\\الحصول على وصل تأسيس الضمانة الادارية .txt', 'file_name': 'الحصول على وصل تأسيس الضمانة الادارية .txt', 'file_type': 'text/plain', 'file_size': 3095, 'creation_date': '2023-12-14', 'last_modified_date': '2023-12-14', 'last_accessed_date': '2023-12-16'}, excluded_embed_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], excluded_llm_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], relationships={}, hash='eca215ab1876fab827b2f5fc08b2ca1a254cb40b12374a53069977e8624b5963', text="الحصول على وصل تأسيس الضمانة الادارية \t\nContent: إدارتي ,الإدارة العمومية ,الشباك ,الخدمة/الخدمات ,البوابة الوطنية للإدارة ,موقع الإدارة المغربية ,أفراد ,مواطنون مغاربة ,سكان مغاربة ,مغاربة مقيمون بالخارج ,أجانب ,سياح ,مهنيين ,مستثمرون ,خواص ,مقاولون ,رجال أعمال ,حرفيون ,مقاولون ذاتيون ,الشركات ,الجبايات ,الضريبة/الضرائب ,السجل التجاري ,شخص معنوي ,الملكية التجارية ,شركة متعددة الجنسيات ,شركة ذات مسؤولية محدودة ,المستثمرون ,المراكز الجهوية للاستثمار ,مشاريع استثمارية ,أسئلة متداولة ,سؤال/جواب ,النصوص القانونية ,النصوص المنظمة ,مرسوم ,ظهير شريف ,نص تشريعي ,نص تنظيمي ,قانون ,أجل الحصول على وثيقة ,أجل الحصول على جواز السفر ,أجل أقصى ,أجل أدنى\nKeywords: ['إدارتي ,الإدارة العمومية ,الشباك ,الخدمة/الخدمات ,البوابة الوطنية للإدارة ,موقع الإدارة المغربية ,أفراد ,مواطنون مغاربة ,سكان مغاربة ,مغاربة مقيمون بالخارج ,أجانب ,سياح ,مهنيين ,مستثمرون ,خواص ,مقاولون ,رجال أعمال ,حرفيون ,مقاولون ذاتيون ,الشركات ,الجبايات ,الضريبة/الضرائب ,السجل التجاري ,شخص معنوي ,الملكية التجارية ,شركة متعددة الجنسيات ,شركة ذات مسؤولية محدودة ,المستثمرون ,المراكز الجهوية للاستثمار ,مشاريع استثمارية ,أسئلة متداولة ,سؤال/جواب ,النصوص القانونية ,النصوص المنظمة ,مرسوم ,ظهير شريف ,نص تشريعي ,نص تنظيمي ,قانون ,أجل الحصول على وثيقة ,أجل الحصول على جواز السفر ,أجل أقصى ,أجل أدنى']\nنوع الإدارة: صندوق الإيداع والتدبير\nملخص: الحصول على وصل تأسيس الضمانة الادارية \t\t\t\t\t\nالوثائق اللازمة: \nالمصلحة المكلفة باستلام الطلب : صندوق الإيداع والتدبير, وزارة الاقتصاد والمالية وإصلاح الإدارة-الخزينة العامة للمملكة, \nالمصلحة المكلفة بالتسيلم : صندوق الإيداع والتدبير, وزارة الاقتصاد والمالية وإصلاح الإدارة-الخزينة العامة للمملكة, \nوثائق للتحميل : , \nأجل معالجة الطلب وتسليم القرار الإداري : يومان\n : 2 يوم; يومان\n : 2 يوم, \nالتكلفة : رسم التنبر0,025% من مبلغ الكفالة\n, \n", start_char_idx=None, end_char_idx=None, text_template='{metadata_str}\n\n{content}', metadata_template='{key}: {value}', metadata_seperator='\n'), Document(id_='6680959a-41c3-45fd-8de2-1e652de26b03', embedding=None, metadata={'file_path': 'D:\\MoroccanAI\\Hackathon1\\Streamlit\\المقاولة والأعمال\\الصفقات العمومية\\الحصول على وصل تأسيس الضمانة المؤقتة للراغبين في المزايدة والمناقصة .txt', 'file_name': 'الحصول على وصل تأسيس الضمانة المؤقتة للراغبين في المزايدة والمناقصة .txt', 'file_type': 'text/plain', 'file_size': 3227, 'creation_date': '2023-12-13', 'last_modified_date': '2023-12-13', 'last_accessed_date': '2023-12-16'}, excluded_embed_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], excluded_llm_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], relationships={}, hash='92e5fd7f1963bf49cffaf018b1a8ee146638eff43263b46cf51dfef32364ee8d', text="الحصول على وصل تأسيس الضمانة المؤقتة للراغبين في المزايدة والمناقصة \t\nContent: إدارتي ,الإدارة العمومية ,الشباك ,الخدمة/الخدمات ,البوابة الوطنية للإدارة ,موقع الإدارة المغربية ,أفراد ,مواطنون مغاربة ,سكان مغاربة ,مغاربة مقيمون بالخارج ,أجانب ,سياح ,مهنيين ,مستثمرون ,خواص ,مقاولون ,رجال أعمال ,حرفيون ,مقاولون ذاتيون ,الشركات ,الجبايات ,الضريبة/الضرائب ,السجل التجاري ,شخص معنوي ,الملكية التجارية ,شركة متعددة الجنسيات ,شركة ذات مسؤولية محدودة ,المستثمرون ,المراكز الجهوية للاستثمار ,مشاريع استثمارية ,أسئلة متداولة ,سؤال/جواب ,النصوص القانونية ,النصوص المنظمة ,مرسوم ,ظهير شريف ,نص تشريعي ,نص تنظيمي ,قانون ,أجل الحصول على وثيقة ,أجل الحصول على جواز السفر ,أجل أقصى ,أجل أدنى\nKeywords: ['إدارتي ,الإدارة العمومية ,الشباك ,الخدمة/الخدمات ,البوابة الوطنية للإدارة ,موقع الإدارة المغربية ,أفراد ,مواطنون مغاربة ,سكان مغاربة ,مغاربة مقيمون بالخارج ,أجانب ,سياح ,مهنيين ,مستثمرون ,خواص ,مقاولون ,رجال أعمال ,حرفيون ,مقاولون ذاتيون ,الشركات ,الجبايات ,الضريبة/الضرائب ,السجل التجاري ,شخص معنوي ,الملكية التجارية ,شركة متعددة الجنسيات ,شركة ذات مسؤولية محدودة ,المستثمرون ,المراكز الجهوية للاستثمار ,مشاريع استثمارية ,أسئلة متداولة ,سؤال/جواب ,النصوص القانونية ,النصوص المنظمة ,مرسوم ,ظهير شريف ,نص تشريعي ,نص تنظيمي ,قانون ,أجل الحصول على وثيقة ,أجل الحصول على جواز السفر ,أجل أقصى ,أجل أدنى']\nنوع الإدارة: صندوق الإيداع والتدبير\nملخص: تأسيس الضمانة المؤقتة للراغبين في المزايدة أوالمناقصة\t\nالوثائق اللازمة: المطبوع الخاص بالضمانة المؤقتة مملوء وموقع, شِيكٌ مُصَدَّق عَلَيْهِ من قبل البنك بمبلغ الكفالة, \nالمصلحة المكلفة باستلام الطلب : صندوق الإيداع والتدبير, وزارة الاقتصاد والمالية وإصلاح الإدارة-الخزينة العامة للمملكة, \nالمصلحة المكلفة بالتسيلم : صندوق الإيداع والتدبير, وزارة الاقتصاد والمالية وإصلاح الإدارة-الخزينة العامة للمملكة, \nوثائق للتحميل : , \nالتكلفة : رسم التنبر0,025% من مبلغ الكفالة\n, \n", start_char_idx=None, end_char_idx=None, text_template='{metadata_str}\n\n{content}', metadata_template='{key}: {value}', metadata_seperator='\n'), Document(id_='38860d37-3b3a-4465-bf27-bec8635aad51', embedding=None, metadata={'file_path': 'D:\\MoroccanAI\\Hackathon1\\Streamlit\\المقاولة والأعمال\\الصفقات العمومية\\الحصول على وصل ضمان وكالة التشغيل الخاصة .txt', 'file_name': 'الحصول على وصل ضمان وكالة التشغيل الخاصة .txt', 'file_type': 'text/plain', 'file_size': 3374, 'creation_date': '2023-12-14', 'last_modified_date': '2023-12-14', 'last_accessed_date': '2023-12-16'}, excluded_embed_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], excluded_llm_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], relationships={}, hash='3e4bbaf481af9a8213cfbcf955343011dc56466157873c55248dd1f23777c09a', text="الحصول على وصل ضمان وكالة التشغيل الخاصة \nContent: إدارتي ,الإدارة العمومية ,الشباك ,الخدمة/الخدمات ,البوابة الوطنية للإدارة ,موقع الإدارة المغربية ,أفراد ,مواطنون مغاربة ,سكان مغاربة ,مغاربة مقيمون بالخارج ,أجانب ,سياح ,مهنيين ,مستثمرون ,خواص ,مقاولون ,رجال أعمال ,حرفيون ,مقاولون ذاتيون ,الشركات ,الجبايات ,الضريبة/الضرائب ,السجل التجاري ,شخص معنوي ,الملكية التجارية ,شركة متعددة الجنسيات ,شركة ذات مسؤولية محدودة ,المستثمرون ,المراكز الجهوية للاستثمار ,مشاريع استثمارية ,أسئلة متداولة ,سؤال/جواب ,النصوص القانونية ,النصوص المنظمة ,مرسوم ,ظهير شريف ,نص تشريعي ,نص تنظيمي ,قانون ,أجل الحصول على وثيقة ,أجل الحصول على جواز السفر ,أجل أقصى ,أجل أدنى\nKeywords: ['إدارتي ,الإدارة العمومية ,الشباك ,الخدمة/الخدمات ,البوابة الوطنية للإدارة ,موقع الإدارة المغربية ,أفراد ,مواطنون مغاربة ,سكان مغاربة ,مغاربة مقيمون بالخارج ,أجانب ,سياح ,مهنيين ,مستثمرون ,خواص ,مقاولون ,رجال أعمال ,حرفيون ,مقاولون ذاتيون ,الشركات ,الجبايات ,الضريبة/الضرائب ,السجل التجاري ,شخص معنوي ,الملكية التجارية ,شركة متعددة الجنسيات ,شركة ذات مسؤولية محدودة ,المستثمرون ,المراكز الجهوية للاستثمار ,مشاريع استثمارية ,أسئلة متداولة ,سؤال/جواب ,النصوص القانونية ,النصوص المنظمة ,مرسوم ,ظهير شريف ,نص تشريعي ,نص تنظيمي ,قانون ,أجل الحصول على وثيقة ,أجل الحصول على جواز السفر ,أجل أقصى ,أجل أدنى']\nنوع الإدارة: صندوق الإيداع والتدبير\nملخص: تأسيس ضمانة وكالة التشغيل الخاصة \nالوثائق اللازمة: المطبوع الخاص بوكالة التشغيل معبأ وموقع, شِيكٌ مُصَدَّق عَلَيْهِ من قبل البنك بمبلغ الكفالة, رسالة وزارة الشغل موجهة الى وكالة التشغيل قصد تكوين الكفالة أصلية , \nالمصلحة المكلفة باستلام الطلب : صندوق الإيداع والتدبير, وزارة الاقتصاد والمالية وإصلاح الإدارة-الخزينة العامة للمملكة, \nالمصلحة المكلفة بالتسيلم : صندوق الإيداع والتدبير, وزارة الاقتصاد والمالية وإصلاح الإدارة-الخزينة العامة للمملكة, \nوثائق للتحميل : , \nأجل معالجة الطلب وتسليم القرار الإداري : يومان : 2 يوم; يومان : 2 يوم, \nالتكلفة : رسم التنبر0,025% من مبلغ الكفالة\n, \n", start_char_idx=None, end_char_idx=None, text_template='{metadata_str}\n\n{content}', metadata_template='{key}: {value}', metadata_seperator='\n'), Document(id_='1a2c2122-2343-4be8-91d8-88617bfc6455', embedding=None, metadata={'file_path': 'D:\\MoroccanAI\\Hackathon1\\Streamlit\\المقاولة والأعمال\\الصفقات العمومية\\الحصول على وصل و التصريح بتأسيس الضمانة النهائية في مجال الصفقات العمومية .txt', 'file_name': 'الحصول على وصل و التصريح بتأسيس الضمانة النهائية في مجال الصفقات العمومية .txt', 'file_type': 'text/plain', 'file_size': 3388, 'creation_date': '2023-12-14', 'last_modified_date': '2023-12-14', 'last_accessed_date': '2023-12-16'}, excluded_embed_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], excluded_llm_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], relationships={}, hash='f50bd4787e9d9a68e53fdadc979ef6c4acbdcd5a40faf17544b7fcb9173ef4b2', text="الحصول على وصل و التصريح بتأسيس الضمانة النهائية في مجال الصفقات العمومية \nContent: إدارتي ,الإدارة العمومية ,الشباك ,الخدمة/الخدمات ,البوابة الوطنية للإدارة ,موقع الإدارة المغربية ,أفراد ,مواطنون مغاربة ,سكان مغاربة ,مغاربة مقيمون بالخارج ,أجانب ,سياح ,مهنيين ,مستثمرون ,خواص ,مقاولون ,رجال أعمال ,حرفيون ,مقاولون ذاتيون ,الشركات ,الجبايات ,الضريبة/الضرائب ,السجل التجاري ,شخص معنوي ,الملكية التجارية ,شركة متعددة الجنسيات ,شركة ذات مسؤولية محدودة ,المستثمرون ,المراكز الجهوية للاستثمار ,مشاريع استثمارية ,أسئلة متداولة ,سؤال/جواب ,النصوص القانونية ,النصوص المنظمة ,مرسوم ,ظهير شريف ,نص تشريعي ,نص تنظيمي ,قانون ,أجل الحصول على وثيقة ,أجل الحصول على جواز السفر ,أجل أقصى ,أجل أدنى\nKeywords: ['إدارتي ,الإدارة العمومية ,الشباك ,الخدمة/الخدمات ,البوابة الوطنية للإدارة ,موقع الإدارة المغربية ,أفراد ,مواطنون مغاربة ,سكان مغاربة ,مغاربة مقيمون بالخارج ,أجانب ,سياح ,مهنيين ,مستثمرون ,خواص ,مقاولون ,رجال أعمال ,حرفيون ,مقاولون ذاتيون ,الشركات ,الجبايات ,الضريبة/الضرائب ,السجل التجاري ,شخص معنوي ,الملكية التجارية ,شركة متعددة الجنسيات ,شركة ذات مسؤولية محدودة ,المستثمرون ,المراكز الجهوية للاستثمار ,مشاريع استثمارية ,أسئلة متداولة ,سؤال/جواب ,النصوص القانونية ,النصوص المنظمة ,مرسوم ,ظهير شريف ,نص تشريعي ,نص تنظيمي ,قانون ,أجل الحصول على وثيقة ,أجل الحصول على جواز السفر ,أجل أقصى ,أجل أدنى']\nنوع الإدارة: صندوق الإيداع والتدبير\nملخص: الحصول على وصل و التصريح بتأسيس الضمانة النهائية في مجال الصفقات العمومية \nالوثائق اللازمة: المطبوع الخاص بطلب تكوين الضمان النهائي مملوء وموقع, المطبوع الخاص بشهادة تكوين الضمان النهائي مملوء وموقع, شِيكٌ مُصَدَّق عَلَيْهِ من قبل البنك بمبلغ الكفالة, \nالمصلحة المكلفة باستلام الطلب : صندوق الإيداع والتدبير, وزارة الاقتصاد والمالية وإصلاح الإدارة-الخزينة العامة للمملكة, \nالمصلحة المكلفة بالتسيلم : صندوق الإيداع والتدبير, وزارة الاقتصاد والمالية وإصلاح الإدارة-الخزينة العامة للمملكة, \nوثائق للتحميل : , \nالتكلفة : رسم التنبر0,025% من مبلغ الكفالة\n, \n", start_char_idx=None, end_char_idx=None, text_template='{metadata_str}\n\n{content}', metadata_template='{key}: {value}', metadata_seperator='\n'), Document(id_='b9cf6ca8-dc25-4202-8973-970b2058b294', embedding=None, metadata={'file_path': 'D:\\MoroccanAI\\Hackathon1\\Streamlit\\المقاولة والأعمال\\الصفقات العمومية\\المشاركة في عروض الأثمان لكراء حق الصيد بالمياه البرية.txt', 'file_name': 'المشاركة في عروض الأثمان لكراء حق الصيد بالمياه البرية.txt', 'file_type': 'text/plain', 'file_size': 5401, 'creation_date': '2023-12-14', 'last_modified_date': '2023-12-14', 'last_accessed_date': '2023-12-16'}, excluded_embed_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], excluded_llm_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], relationships={}, hash='1ad123f8020e5b88543371372d47625d1530927ffb49e1b5c1e71e910357290c', text='المشاركة في عروض الأثمان لكراء حق الصيد بالمياه البرية\nContent: إدارتي ,الإدارة العمومية ,الشباك ,الخدمة/الخدمات ,البوابة الوطنية للإدارة ,موقع الإدارة المغربية ,أفراد ,مواطنون مغاربة ,سكان مغاربة ,مغاربة مقيمون بالخارج ,أجانب ,سياح ,مهنيين ,مستثمرون ,خواص ,مقاولون ,رجال أعمال ,حرفيون ,مقاولون ذاتيون ,الشركات ,الجبايات ,الضريبة/الضرائب ,السجل التجاري ,شخص معنوي ,الملكية التجارية ,شركة متعددة الجنسيات ,شركة ذات مسؤولية محدودة ,المستثمرون ,المراكز الجهوية للاستثمار ,مشاريع استثمارية ,أسئلة متداولة ,سؤال/جواب ,النصوص القانونية ,النصوص المنظمة ,مرسوم ,ظهير شريف ,نص تشريعي ,نص تنظيمي ,قانون ,أجل الحصول على وثيقة ,أجل الحصول على جواز السفر ,أجل أقصى ,أجل أدنى\nKeywords: [\'إدارتي ,الإدارة العمومية ,الشباك ,الخدمة/الخدمات ,البوابة الوطنية للإدارة ,موقع الإدارة المغربية ,أفراد ,مواطنون مغاربة ,سكان مغاربة ,مغاربة مقيمون بالخارج ,أجانب ,سياح ,مهنيين ,مستثمرون ,خواص ,مقاولون ,رجال أعمال ,حرفيون ,مقاولون ذاتيون ,الشركات ,الجبايات ,الضريبة/الضرائب ,السجل التجاري ,شخص معنوي ,الملكية التجارية ,شركة متعددة الجنسيات ,شركة ذات مسؤولية محدودة ,المستثمرون ,المراكز الجهوية للاستثمار ,مشاريع استثمارية ,أسئلة متداولة ,سؤال/جواب ,النصوص القانونية ,النصوص المنظمة ,مرسوم ,ظهير شريف ,نص تشريعي ,نص تنظيمي ,قانون ,أجل الحصول على وثيقة ,أجل الحصول على جواز السفر ,أجل أقصى ,أجل أدنى\']\nنوع الإدارة: الوكالة الوطنية للمياه والغابات\nملخص: المشاركة في عروض الأثمان\nالوثائق اللازمة: طلب الايجار, بالنسبة للجمعيات:, نسخة من القانون الأساسي للجمعية, نسخة من محضر الجمع العام التأسيسي, وصل إيداع القانون الأساسي لدى السلطات المحلية, قائمة أعضاء المكتب وقائمة المنخرطين, بالنسبة لتعاونيات الصيد:, نسخة من القانون الأساسي, نسخة من القانون الداخلي للتعاونية, نسخة من الـتسـجيــل فــي الســجـل المحلي للتعاونيات, نسخة من محضر الجمع العام التأسيسي الأخير , قائمة أعضاء المكتب وقائمة المنخرطين, بالنسبة لشركات الصيد:, نسخة من القانون الأساسي للشركة (يجب أن يكون موضوع الشركة يخص ممارسة الصيد أو تربية الأحياء المائية أو نشاط مماثل) , شهادة القيد في السجل التجاري, شهادة منذ أقل من سنة من طرف اﻟصندوق اﻟوطﻧﻲ ﻟﻟﺿﻣﺎن اﻻﺟﺗﻣﺎﻋﻲ تثبت أن المنافس ﻳﻮﺟﺪ ﻓﻲ وﺿﻌﻴﺔ ﻗﺎﻧﻮﻧﻴﺔ اﺗﺠﺎﻩ هﺬا اﻟﺼﻨﺪوق, شهادة منذ أقل من سنة من طرف القابض في محل فرض الضريبة تثبت أن المنافس ﻳﻮﺟﺪ في وضعية جبائية قانونية, وصل الإيداع للضمان المؤقت, دفتر التحملات الخاص وتأشير جميع الصفحات مع إمضاء الأخيرة بالميزة " قُرِأَ وَقُبِلَ ", العرض التقني الذي يحدد الميزانية المخصصة لبرنامج تهيئة مصايد السمكية المقترحة من طرف المتنافس, مذكرة توضح الأعمال المقترحة لاستغلال مستدام للثروة السمكية، لاسيما من خلال التزام المتنافس بالتثمين السمكي للمصايد عبر عمليات التهيئة أو بعمليات الإستزراع أو هما معا, مذكرة توضح عدد مناصب الشغل المراد إحداثها وكذا الإجراءات المتخذة لتأطير الصيادين، ولاسيما في مجال الصيد المسؤول, العرض المالي يبين قدر الإيجار السنوي لكراء حق الصيد, \nالمصلحة المكلفة باستلام الطلب : المديريات الجهوية للمياه والغابات ومحاربة التصحر, \nالمصلحة المكلفة بالتسيلم : المديريات الجهوية للمياه والغابات ومحاربة التصحر, \nوثائق للتحميل : , \nأجل معالجة الطلب وتسليم القرار الإداري : 30 يوما : 30 يوما; 30 يوما : 30 يوما, \nالتكلفة : بالمجان\n, \n', start_char_idx=None, end_char_idx=None, text_template='{metadata_str}\n\n{content}', metadata_template='{key}: {value}', metadata_seperator='\n'), Document(id_='e106725a-ca89-4154-8b46-a178757fffdd', embedding=None, metadata={'file_path': 'D:\\MoroccanAI\\Hackathon1\\Streamlit\\المقاولة والأعمال\\الصفقات العمومية\\شهادة الوضعية الجبائية من أجل المشاركة في الصفقات العمومية  (P203).txt', 'file_name': 'شهادة الوضعية الجبائية من أجل المشاركة في الصفقات العمومية  (P203).txt', 'file_type': 'text/plain', 'file_size': 3272, 'creation_date': '2023-12-13', 'last_modified_date': '2023-12-13', 'last_accessed_date': '2023-12-16'}, excluded_embed_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], excluded_llm_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], relationships={}, hash='d686a25d4ca915e0d07af83395554dfc9cde5cca1633153092a782fa28c4f82b', text="شهادة الوضعية الجبائية من أجل المشاركة في الصفقات العمومية  (P203)\nContent: إدارتي ,الإدارة العمومية ,الشباك ,الخدمة/الخدمات ,البوابة الوطنية للإدارة ,موقع الإدارة المغربية ,أفراد ,مواطنون مغاربة ,سكان مغاربة ,مغاربة مقيمون بالخارج ,أجانب ,سياح ,مهنيين ,مستثمرون ,خواص ,مقاولون ,رجال أعمال ,حرفيون ,مقاولون ذاتيون ,الشركات ,الجبايات ,الضريبة/الضرائب ,السجل التجاري ,شخص معنوي ,الملكية التجارية ,شركة متعددة الجنسيات ,شركة ذات مسؤولية محدودة ,المستثمرون ,المراكز الجهوية للاستثمار ,مشاريع استثمارية ,أسئلة متداولة ,سؤال/جواب ,النصوص القانونية ,النصوص المنظمة ,مرسوم ,ظهير شريف ,نص تشريعي ,نص تنظيمي ,قانون ,أجل الحصول على وثيقة ,أجل الحصول على جواز السفر ,أجل أقصى ,أجل أدنى\nKeywords: ['إدارتي ,الإدارة العمومية ,الشباك ,الخدمة/الخدمات ,البوابة الوطنية للإدارة ,موقع الإدارة المغربية ,أفراد ,مواطنون مغاربة ,سكان مغاربة ,مغاربة مقيمون بالخارج ,أجانب ,سياح ,مهنيين ,مستثمرون ,خواص ,مقاولون ,رجال أعمال ,حرفيون ,مقاولون ذاتيون ,الشركات ,الجبايات ,الضريبة/الضرائب ,السجل التجاري ,شخص معنوي ,الملكية التجارية ,شركة متعددة الجنسيات ,شركة ذات مسؤولية محدودة ,المستثمرون ,المراكز الجهوية للاستثمار ,مشاريع استثمارية ,أسئلة متداولة ,سؤال/جواب ,النصوص القانونية ,النصوص المنظمة ,مرسوم ,ظهير شريف ,نص تشريعي ,نص تنظيمي ,قانون ,أجل الحصول على وثيقة ,أجل الحصول على جواز السفر ,أجل أقصى ,أجل أدنى']\nنوع الإدارة: وزارة الاقتصاد والمالية-الخزينة العامة للمملكة\nملخص: من أجل المشاركة في الصفقات العمومية  \nالوثائق اللازمة: طلب الحصول على الشهادة الجبائية للمتعهدين في الصفقات العمومية   (P203), شهادة مسلمة من طرف مصالح الوعاء الضريبي, إشهاد مسلم من طرف مصالح الوعاء المكلفة بالجبايات الترابية, \nالمصلحة المكلفة باستلام الطلب : القباضات التابعة للخزينة العامة للمملكة, \nالمصلحة المكلفة بالتسيلم : القباضات التابعة للخزينة العامة للمملكة, \nوثائق للتحميل : , \nأجل معالجة الطلب وتسليم القرار الإداري : 5 أيام : 5 ايام; 5 أيام : 5 ايام, \nالتكلفة : بالمجان, \n", start_char_idx=None, end_char_idx=None, text_template='{metadata_str}\n\n{content}', metadata_template='{key}: {value}', metadata_seperator='\n'), Document(id_='e863206a-d9a7-47cc-96af-b72a099e3e91', embedding=None, metadata={'file_path': 'D:\\MoroccanAI\\Hackathon1\\Streamlit\\المقاولة والأعمال\\الصفقات العمومية\\شهادة للمشاركة في الصفقات العمومية (Invest).txt', 'file_name': 'شهادة للمشاركة في الصفقات العمومية (Invest).txt', 'file_type': 'text/plain', 'file_size': 3496, 'creation_date': '2023-12-13', 'last_modified_date': '2023-12-13', 'last_accessed_date': '2023-12-16'}, excluded_embed_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], excluded_llm_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], relationships={}, hash='9500c5c30de35202b5400fdc774a1ce1a49466e1d5e04610b8db4f071778649f', text="شهادة للمشاركة في الصفقات العمومية (Invest)\nContent: إدارتي ,الإدارة العمومية ,الشباك ,الخدمة/الخدمات ,البوابة الوطنية للإدارة ,موقع الإدارة المغربية ,أفراد ,مواطنون مغاربة ,سكان مغاربة ,مغاربة مقيمون بالخارج ,أجانب ,سياح ,مهنيين ,مستثمرون ,خواص ,مقاولون ,رجال أعمال ,حرفيون ,مقاولون ذاتيون ,الشركات ,الجبايات ,الضريبة/الضرائب ,السجل التجاري ,شخص معنوي ,الملكية التجارية ,شركة متعددة الجنسيات ,شركة ذات مسؤولية محدودة ,المستثمرون ,المراكز الجهوية للاستثمار ,مشاريع استثمارية ,أسئلة متداولة ,سؤال/جواب ,النصوص القانونية ,النصوص المنظمة ,مرسوم ,ظهير شريف ,نص تشريعي ,نص تنظيمي ,قانون ,أجل الحصول على وثيقة ,أجل الحصول على جواز السفر ,أجل أقصى ,أجل أدنى\nKeywords: ['إدارتي ,الإدارة العمومية ,الشباك ,الخدمة/الخدمات ,البوابة الوطنية للإدارة ,موقع الإدارة المغربية ,أفراد ,مواطنون مغاربة ,سكان مغاربة ,مغاربة مقيمون بالخارج ,أجانب ,سياح ,مهنيين ,مستثمرون ,خواص ,مقاولون ,رجال أعمال ,حرفيون ,مقاولون ذاتيون ,الشركات ,الجبايات ,الضريبة/الضرائب ,السجل التجاري ,شخص معنوي ,الملكية التجارية ,شركة متعددة الجنسيات ,شركة ذات مسؤولية محدودة ,المستثمرون ,المراكز الجهوية للاستثمار ,مشاريع استثمارية ,أسئلة متداولة ,سؤال/جواب ,النصوص القانونية ,النصوص المنظمة ,مرسوم ,ظهير شريف ,نص تشريعي ,نص تنظيمي ,قانون ,أجل الحصول على وثيقة ,أجل الحصول على جواز السفر ,أجل أقصى ,أجل أدنى']\nنوع الإدارة: الصندوق الوطني للضمان الاجتماعي\nملخص: الحصول على شهادة للمشاركة في الصفقات العمومية\nيخضع هذا القرار لمقتضيات المرسوم رقم 2.22.385 بتحديد لائحة القرارات الإدارية اللازمة لإنجاز مشاريع الإستثمار التي لا يتجاوز أجل معالجة الطلبات المتعلقة بها وتسليمها 30 يوما\n\nالوثائق اللازمة: طلب الشهادة يحمل إمضاء و خاتم المنخرط و يبين :الاسم أو الاسم التجاري , رمز شهادة التعريف الموحد , عنوان المقر الاجتماعي و رقم الانخراط, \nالمصلحة المكلفة باستلام الطلب : المديريات الجهوية ووكالات الصندوق الوطني للضمان الاجتماعي, \nالمصلحة المكلفة بالتسيلم : المديريات الجهوية ووكالات الصندوق الوطني للضمان الاجتماعي, \nوثائق للتحميل : , \nأجل معالجة الطلب وتسليم القرار الإداري : 2 يوم, \nالتكلفة : بالمجان , \n", start_char_idx=None, end_char_idx=None, text_template='{metadata_str}\n\n{content}', metadata_template='{key}: {value}', metadata_seperator='\n'), Document(id_='bb24bac9-2652-47e7-8783-ecd391afbb9c', embedding=None, metadata={'file_path': 'D:\\MoroccanAI\\Hackathon1\\Streamlit\\المقاولة والأعمال\\الصفقات العمومية\\طلب استرجاع الضمانة المؤقتة عن طريق تحويل بنكي.txt', 'file_name': 'طلب استرجاع الضمانة المؤقتة عن طريق تحويل بنكي.txt', 'file_type': 'text/plain', 'file_size': 4166, 'creation_date': '2023-12-13', 'last_modified_date': '2023-12-13', 'last_accessed_date': '2023-12-16'}, excluded_embed_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], excluded_llm_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], relationships={}, hash='d60f0d4daf3f4759119af4f9ae47402f14ea7e0f65ee4963db59e431ee752177', text="طلب استرجاع الضمانة المؤقتة عن طريق تحويل بنكي\nContent: إدارتي ,الإدارة العمومية ,الشباك ,الخدمة/الخدمات ,البوابة الوطنية للإدارة ,موقع الإدارة المغربية ,أفراد ,مواطنون مغاربة ,سكان مغاربة ,مغاربة مقيمون بالخارج ,أجانب ,سياح ,مهنيين ,مستثمرون ,خواص ,مقاولون ,رجال أعمال ,حرفيون ,مقاولون ذاتيون ,الشركات ,الجبايات ,الضريبة/الضرائب ,السجل التجاري ,شخص معنوي ,الملكية التجارية ,شركة متعددة الجنسيات ,شركة ذات مسؤولية محدودة ,المستثمرون ,المراكز الجهوية للاستثمار ,مشاريع استثمارية ,أسئلة متداولة ,سؤال/جواب ,النصوص القانونية ,النصوص المنظمة ,مرسوم ,ظهير شريف ,نص تشريعي ,نص تنظيمي ,قانون ,أجل الحصول على وثيقة ,أجل الحصول على جواز السفر ,أجل أقصى ,أجل أدنى\nKeywords: ['إدارتي ,الإدارة العمومية ,الشباك ,الخدمة/الخدمات ,البوابة الوطنية للإدارة ,موقع الإدارة المغربية ,أفراد ,مواطنون مغاربة ,سكان مغاربة ,مغاربة مقيمون بالخارج ,أجانب ,سياح ,مهنيين ,مستثمرون ,خواص ,مقاولون ,رجال أعمال ,حرفيون ,مقاولون ذاتيون ,الشركات ,الجبايات ,الضريبة/الضرائب ,السجل التجاري ,شخص معنوي ,الملكية التجارية ,شركة متعددة الجنسيات ,شركة ذات مسؤولية محدودة ,المستثمرون ,المراكز الجهوية للاستثمار ,مشاريع استثمارية ,أسئلة متداولة ,سؤال/جواب ,النصوص القانونية ,النصوص المنظمة ,مرسوم ,ظهير شريف ,نص تشريعي ,نص تنظيمي ,قانون ,أجل الحصول على وثيقة ,أجل الحصول على جواز السفر ,أجل أقصى ,أجل أدنى']\nنوع الإدارة: صندوق الإيداع والتدبير\nملخص: طلب استرجاع الضمانة المؤقتة عن طريق تحويل بنكي\nالوثائق اللازمة: شهادة رفع اليد مسلمة من قبل صاحب الصفقة, وصل الإيداع الأصلي, طلب المناقص/ المزايد, شهادة التعريف البنكي الخاصة بالمناقص / المزايد, في حالة ضياع وصل الدفع:شهادة ضياع محررة من قبل المناقص / المزايد أمام السلطات المختصه + نسخة من القانون الاساسي للشركة, في حالة ارسال وصل الدفع من قبل مالك الصفقة مع وثائق الأداء: شهادة مسلمة من قبل مالك الصفقة تثبت ذلك, في حالة تجمع الشركات: شهادة حساب بنكي مشترك, في حالة عدم مشاركة المناقص/ المزايد: شهادة عدم الامشاركة في المناقصة/ المزايدة مسلمة من قبل مالك الصفقة, وصل الإيداع الأصلي, في حالة تقديم الضمان المؤقت لدى صندوق الإيداع والتدبير بعد سنتين من تأسيسه بالخزينة العامة: شهادة عدم الأداء مسلمة من قبل محاسب الخزينة الذي تم تأسيس الضمان لديه, \nالمصلحة المكلفة باستلام الطلب : الخزينة العامة للمملكة, صندوق الإيداع والتدبير, \nالمصلحة المكلفة بالتسيلم : الخزينة العامة للمملكة, صندوق الإيداع والتدبير, \nوثائق للتحميل : , \nأجل معالجة الطلب وتسليم القرار الإداري : 60 يوما : 60 يوما; 60 يوما : 60 يوما, \nالتكلفة : بالمجان, \n", start_char_idx=None, end_char_idx=None, text_template='{metadata_str}\n\n{content}', metadata_template='{key}: {value}', metadata_seperator='\n'), Document(id_='db231131-c794-4038-ab63-d930fb367adf', embedding=None, metadata={'file_path': 'D:\\MoroccanAI\\Hackathon1\\Streamlit\\المقاولة والأعمال\\الصفقات العمومية\\طلب استرجاع الضمانة المؤقتة لدى وكالة فرع الرباط بالنسبة للأشخاص الطبيعيين الذين لايتوفرون على حساب بنكي.txt', 'file_name': 'طلب استرجاع الضمانة المؤقتة لدى وكالة فرع الرباط بالنسبة للأشخاص الطبيعيين الذين لايتوفرون على حساب بنكي.txt', 'file_type': 'text/plain', 'file_size': 5398, 'creation_date': '2023-12-13', 'last_modified_date': '2023-12-13', 'last_accessed_date': '2023-12-16'}, excluded_embed_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], excluded_llm_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], relationships={}, hash='5f683f609f517267f925134ff8e3fb4e94150565e8e2f68f90ad8c96e00b40c4', text="طلب استرجاع الضمانة المؤقتة لدى وكالة فرع الرباط بالنسبة للأشخاص الطبيعيين الذين لايتوفرون على حساب بنكي\nContent: إدارتي ,الإدارة العمومية ,الشباك ,الخدمة/الخدمات ,البوابة الوطنية للإدارة ,موقع الإدارة المغربية ,أفراد ,مواطنون مغاربة ,سكان مغاربة ,مغاربة مقيمون بالخارج ,أجانب ,سياح ,مهنيين ,مستثمرون ,خواص ,مقاولون ,رجال أعمال ,حرفيون ,مقاولون ذاتيون ,الشركات ,الجبايات ,الضريبة/الضرائب ,السجل التجاري ,شخص معنوي ,الملكية التجارية ,شركة متعددة الجنسيات ,شركة ذات مسؤولية محدودة ,المستثمرون ,المراكز الجهوية للاستثمار ,مشاريع استثمارية ,أسئلة متداولة ,سؤال/جواب ,النصوص القانونية ,النصوص المنظمة ,مرسوم ,ظهير شريف ,نص تشريعي ,نص تنظيمي ,قانون ,أجل الحصول على وثيقة ,أجل الحصول على جواز السفر ,أجل أقصى ,أجل أدنى\nKeywords: ['إدارتي ,الإدارة العمومية ,الشباك ,الخدمة/الخدمات ,البوابة الوطنية للإدارة ,موقع الإدارة المغربية ,أفراد ,مواطنون مغاربة ,سكان مغاربة ,مغاربة مقيمون بالخارج ,أجانب ,سياح ,مهنيين ,مستثمرون ,خواص ,مقاولون ,رجال أعمال ,حرفيون ,مقاولون ذاتيون ,الشركات ,الجبايات ,الضريبة/الضرائب ,السجل التجاري ,شخص معنوي ,الملكية التجارية ,شركة متعددة الجنسيات ,شركة ذات مسؤولية محدودة ,المستثمرون ,المراكز الجهوية للاستثمار ,مشاريع استثمارية ,أسئلة متداولة ,سؤال/جواب ,النصوص القانونية ,النصوص المنظمة ,مرسوم ,ظهير شريف ,نص تشريعي ,نص تنظيمي ,قانون ,أجل الحصول على وثيقة ,أجل الحصول على جواز السفر ,أجل أقصى ,أجل أدنى']\nنوع الإدارة: صندوق الإيداع والتدبير\nملخص: طلب استرجاع الضمانة المؤقتة لدى وكالة فرع الرباط بالنسبة للأشخاص الطبيعيين الذين لايتوفرون على حساب بنكي\nالوثائق اللازمة: استرجاع الضمانة المؤقتة من قبل المناقص/المزايد:, شهادة رفع اليد مسلمة من قبل صاحب الصفقة, وصل الايداع الاصلي, طلب المناقص / المزايد, شهادة التعريف البنكي الخاصة بالمناقص / المزايد, حالة ضياع وصل الدفع:, شهادة ضياع محررة من قبل المناقص / المزايد أمام السلطات المختصه + نسخة من القانون الاساسي للشركة, شهادة رفع اليد مسلمة من قبل صاحب الصفقة, طلب المناقص / المزايد, شهادة التعريف البنكي الخاصة بالمناقص / المزايد, حالة ضياع وصل الدفع\xa0و تقديم الضمان المؤقت لدى صندوق الايداع والتدبير بعد سنتين من تأسيسه بالخزينة العامة:, شهادة عدم الاداء مسلمة من قبل محاسب الخزينة الذي تم تأسيس الضمان لديه, شهادة ضياع محررة من قبل المناقص / المزايد أمام السلطات المختصه + نسخة من القانون الاساسي للشركة, شهادة رفع اليد مسلمة من قبل صاحب الصفقة, طلب المناقص / المزايد, شهادة التعريف البنكي الخاصة بالمناقص / المزايد, حالة ارسال وصل الدفع من قبل مالك الصفقة مع وثائق الاداء:, شهادة مسلمة من قبل مالك الصفقة تثبت ذلك, شهادة رفع اليد مسلمة من قبل صاحب الصفقة, طلب المناقص / المزايد, شهادة التعريف البنكي الخاصة بالمناقص / المزايد, حالة تجمع الشركات:, شهادة رفع اليد مسلمة من قبل صاحب الصفقة, وصل الايداع الاصلي, طلب المناقص / المزايد, شهادة حساب بنكي مشترك, حالة عدم مشاركة المناقص/المزايد:, شهادة عدم المشاركة في المناقصة/المزايدة مسلمة من قبل مالك الصفقة, وصل الايداع الاصلي, طلب المناقص / المزايد, شهادة حساب بنكي مشترك, \nالمصلحة المكلفة باستلام الطلب : صندوق الإيداع والتدبير, \nالمصلحة المكلفة بالتسيلم : صندوق الإيداع والتدبير, \nوثائق للتحميل : , \nأجل معالجة الطلب وتسليم القرار الإداري : يوم واحد : 1 يوم; يوم واحد : 1 يوم, \nالتكلفة : بالمجان, \n", start_char_idx=None, end_char_idx=None, text_template='{metadata_str}\n\n{content}', metadata_template='{key}: {value}', metadata_seperator='\n'), Document(id_='27bdada8-d208-48c7-9d24-83311e6a3a58', embedding=None, metadata={'file_path': 'D:\\MoroccanAI\\Hackathon1\\Streamlit\\المقاولة والأعمال\\الصفقات العمومية\\طلب استرجاع الضمانة النهائية عن طريق تحويل بنكي.txt', 'file_name': 'طلب استرجاع الضمانة النهائية عن طريق تحويل بنكي.txt', 'file_type': 'text/plain', 'file_size': 5176, 'creation_date': '2023-12-14', 'last_modified_date': '2023-12-14', 'last_accessed_date': '2023-12-16'}, excluded_embed_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], excluded_llm_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], relationships={}, hash='ca4a06e93e1f1232b6c720d8485018c439c8d479b3177e1c07642791b4aa1d79', text="طلب استرجاع الضمانة النهائية عن طريق تحويل بنكي\nContent: إدارتي ,الإدارة العمومية ,الشباك ,الخدمة/الخدمات ,البوابة الوطنية للإدارة ,موقع الإدارة المغربية ,أفراد ,مواطنون مغاربة ,سكان مغاربة ,مغاربة مقيمون بالخارج ,أجانب ,سياح ,مهنيين ,مستثمرون ,خواص ,مقاولون ,رجال أعمال ,حرفيون ,مقاولون ذاتيون ,الشركات ,الجبايات ,الضريبة/الضرائب ,السجل التجاري ,شخص معنوي ,الملكية التجارية ,شركة متعددة الجنسيات ,شركة ذات مسؤولية محدودة ,المستثمرون ,المراكز الجهوية للاستثمار ,مشاريع استثمارية ,أسئلة متداولة ,سؤال/جواب ,النصوص القانونية ,النصوص المنظمة ,مرسوم ,ظهير شريف ,نص تشريعي ,نص تنظيمي ,قانون ,أجل الحصول على وثيقة ,أجل الحصول على جواز السفر ,أجل أقصى ,أجل أدنى\nKeywords: ['إدارتي ,الإدارة العمومية ,الشباك ,الخدمة/الخدمات ,البوابة الوطنية للإدارة ,موقع الإدارة المغربية ,أفراد ,مواطنون مغاربة ,سكان مغاربة ,مغاربة مقيمون بالخارج ,أجانب ,سياح ,مهنيين ,مستثمرون ,خواص ,مقاولون ,رجال أعمال ,حرفيون ,مقاولون ذاتيون ,الشركات ,الجبايات ,الضريبة/الضرائب ,السجل التجاري ,شخص معنوي ,الملكية التجارية ,شركة متعددة الجنسيات ,شركة ذات مسؤولية محدودة ,المستثمرون ,المراكز الجهوية للاستثمار ,مشاريع استثمارية ,أسئلة متداولة ,سؤال/جواب ,النصوص القانونية ,النصوص المنظمة ,مرسوم ,ظهير شريف ,نص تشريعي ,نص تنظيمي ,قانون ,أجل الحصول على وثيقة ,أجل الحصول على جواز السفر ,أجل أقصى ,أجل أدنى']\nنوع الإدارة: صندوق الإيداع والتدبير\nملخص: طلب استرجاع الضمانة النهائية عن طريق تحويل بنكي\nالوثائق اللازمة: استرجاع الضمانة المؤقتة من قبل المناقص/المزايد:, شهادة رفع اليد مسلمة من قبل صاحب الصفقة, وصل الايداع الاصلي, طلب المناقص / المزايد, شهادة التعريف البنكي الخاصة بالمناقص / المزايد, حالة ضياع وصل الدفع, شهادة ضياع محررة من قبل المناقص / المزايد أمام السلطات المختصه + نسخة من القانون الاساسي للشركة, شهادة رفع اليد مسلمة من قبل صاحب الصفقة, طلب المناقص / المزايد, شهادة التعريف البنكي الخاصة بالمناقص / المزايد, حالة ضياع وصل الدفع\xa0و تقديم الضمان المؤقت لدى صندوق الايداع والتدبير بعد سنتين من تأسيسه بالخزينة العامة, شهادة عدم الاداء مسلمة من قبل محاسب الخزينة الذي تم تأسيس الضمان لديه, شهادة ضياع محررة من قبل المناقص / المزايد أمام السلطات المختصه + نسخة من القانون الاساسي للشركة, شهادة رفع اليد مسلمة من قبل صاحب الصفقة, طلب المناقص / المزايد, شهادة التعريف البنكي الخاصة بالمناقص / المزايد, حالة ارسال وصل الدفع من قبل مالك الصفقة مع وثائق الاداء:, شهادة مسلمة من قبل مالك الصفقة تثبت ذلك, شهادة رفع اليد مسلمة من قبل صاحب الصفقة, طلب المناقص / المزايد, شهادة التعريف البنكي الخاصة بالمناقص / المزايد, حالة تجمع الشركات, شهادة رفع اليد مسلمة من قبل صاحب الصفقة, وصل الايداع الاصلي, طلب المناقص / المزايد, شهادة حساب بنكي مشترك, حالة عدم مشاركة المناقص/المزايد, شهادة عدم المشاركة في المناقصة/المزايدة مسلمة من قبل مالك الصفقة, وصل الايداع الاصلي, طلب المناقص / المزايد, شهادة حساب بنكي مشترك, \nالمصلحة المكلفة باستلام الطلب : صندوق الإيداع والتدبير, \nالمصلحة المكلفة بالتسيلم : صندوق الإيداع والتدبير, \nوثائق للتحميل : , \nأجل معالجة الطلب وتسليم القرار الإداري : 60 يوما : 60 يوما; 60 يوما : 60 يوما, \nالتكلفة : مجانا, \n", start_char_idx=None, end_char_idx=None, text_template='{metadata_str}\n\n{content}', metadata_template='{key}: {value}', metadata_seperator='\n'), Document(id_='af5cfa6d-20c3-40d0-9d45-cbe6629e9102', embedding=None, metadata={'file_path': 'D:\\MoroccanAI\\Hackathon1\\Streamlit\\المقاولة والأعمال\\الصفقات العمومية\\طلب استرجاع الضمانة النهائية لدى وكالة فرع الرباط بالنسبة للأشخاص الطبيعيين الذين لايتوفرون على حساب بنكي.txt', 'file_name': 'طلب استرجاع الضمانة النهائية لدى وكالة فرع الرباط بالنسبة للأشخاص الطبيعيين الذين لايتوفرون على حساب بنكي.txt', 'file_type': 'text/plain', 'file_size': 5398, 'creation_date': '2023-12-13', 'last_modified_date': '2023-12-13', 'last_accessed_date': '2023-12-16'}, excluded_embed_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], excluded_llm_metadata_keys=['file_name', 'file_type', 'file_size', 'creation_date', 'last_modified_date', 'last_accessed_date'], relationships={}, hash='68514828f5afb75aead3b9fc9689b904d56cedb025a5bffe547911462bd0021a', text="طلب استرجاع الضمانة النهائية لدى وكالة فرع الرباط بالنسبة للأشخاص الطبيعيين الذين لايتوفرون على حساب بنكي\nContent: إدارتي ,الإدارة العمومية ,الشباك ,الخدمة/الخدمات ,البوابة الوطنية للإدارة ,موقع الإدارة المغربية ,أفراد ,مواطنون مغاربة ,سكان مغاربة ,مغاربة مقيمون بالخارج ,أجانب ,سياح ,مهنيين ,مستثمرون ,خواص ,مقاولون ,رجال أعمال ,حرفيون ,مقاولون ذاتيون ,الشركات ,الجبايات ,الضريبة/الضرائب ,السجل التجاري ,شخص معنوي ,الملكية التجارية ,شركة متعددة الجنسيات ,شركة ذات مسؤولية محدودة ,المستثمرون ,المراكز الجهوية للاستثمار ,مشاريع استثمارية ,أسئلة متداولة ,سؤال/جواب ,النصوص القانونية ,النصوص المنظمة ,مرسوم ,ظهير شريف ,نص تشريعي ,نص تنظيمي ,قانون ,أجل الحصول على وثيقة ,أجل الحصول على جواز السفر ,أجل أقصى ,أجل أدنى\nKeywords: ['إدارتي ,الإدارة العمومية ,الشباك ,الخدمة/الخدمات ,البوابة الوطنية للإدارة ,موقع الإدارة المغربية ,أفراد ,مواطنون مغاربة ,سكان مغاربة ,مغاربة مقيمون بالخارج ,أجانب ,سياح ,مهنيين ,مستثمرون ,خواص ,مقاولون ,رجال أعمال ,حرفيون ,مقاولون ذاتيون ,الشركات ,الجبايات ,الضريبة/الضرائب ,السجل التجاري ,شخص معنوي ,الملكية التجارية ,شركة متعددة الجنسيات ,شركة ذات مسؤولية محدودة ,المستثمرون ,المراكز الجهوية للاستثمار ,مشاريع استثمارية ,أسئلة متداولة ,سؤال/جواب ,النصوص القانونية ,النصوص المنظمة ,مرسوم ,ظهير شريف ,نص تشريعي ,نص تنظيمي ,قانون ,أجل الحصول على وثيقة ,أجل الحصول على جواز السفر ,أجل أقصى ,أجل أدنى']\nنوع الإدارة: صندوق الإيداع والتدبير\nملخص: طلب استرجاع الضمانة النهائية لدى وكالة فرع الرباط بالنسبة للأشخاص الطبيعيين الذين لايتوفرون على حساب بنكي\nالوثائق اللازمة: استرجاع الضمانة المؤقتة من قبل المناقص/المزايد:, شهادة رفع اليد مسلمة من قبل صاحب الصفقة, وصل الايداع الاصلي, طلب المناقص / المزايد, شهادة التعريف البنكي الخاصة بالمناقص / المزايد, حالة ضياع وصل الدفع, شهادة ضياع محررة من قبل المناقص / المزايد أمام السلطات المختصه + نسخة من القانون الاساسي للشركة, شهادة رفع اليد مسلمة من قبل صاحب الصفقة, طلب المناقص / المزايد, شهادة التعريف البنكي الخاصة بالمناقص / المزايد, حالة ضياع وصل الدفع\xa0و تقديم الضمان المؤقت لدى صندوق الايداع والتدبير بعد سنتين من تأسيسه بالخزينة العامة, شهادة عدم الاداء مسلمة من قبل محاسب الخزينة الذي تم تأسيس الضمان لديه, شهادة ضياع محررة من قبل المناقص / المزايد أمام السلطات المختصه + نسخة من القانون الاساسي للشركة, شهادة رفع اليد مسلمة من قبل صاحب الصفقة, طلب المناقص / المزايد, شهادة التعريف البنكي الخاصة بالمناقص / المزايد, حالة ارسال وصل الدفع من قبل مالك الصفقة مع وثائق الاداء:, شهادة مسلمة من قبل مالك الصفقة تثبت ذلك, شهادة رفع اليد مسلمة من قبل صاحب الصفقة, طلب المناقص / المزايد, شهادة التعريف البنكي الخاصة بالمناقص / المزايد, حالة تجمع الشركات, شهادة رفع اليد مسلمة من قبل صاحب الصفقة, وصل الايداع الاصلي, طلب المناقص / المزايد, شهادة حساب بنكي مشترك, حالة عدم مشاركة المناقص/المزايد, شهادة عدم المشاركة في المناقصة/المزايدة مسلمة من قبل مالك الصفقة, وصل الايداع الاصلي, طلب المناقص / المزايد, شهادة حساب بنكي مشترك, \nالمصلحة المكلفة باستلام الطلب : صندوق الإيداع والتدبير, \nالمصلحة المكلفة بالتسيلم : صندوق الإيداع والتدبير, \nوثائق للتحميل : , \nأجل معالجة الطلب وتسليم القرار الإداري : يوم واحد : 1 يوم; يوم واحد : 1 يوم, \nالتكلفة : بالمجان, \n", start_char_idx=None, end_char_idx=None, text_template='{metadata_str}\n\n{content}', metadata_template='{key}: {value}', metadata_seperator='\n')]
            index = VectorStoreIndex.from_documents(documents)
            # store it for later
            index.storage_context.persist()
        else:
            # load the existing index
            storage_context = StorageContext.from_defaults(persist_dir="./storage")
            index = load_index_from_storage(storage_context)
        return index
index = load_index()


if "chat_engine" not in st.session_state.keys(): # Initialize the chat engine
        st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)
# either way we can now query the index
# query_engine = index.as_query_engine()

if prompt := st.chat_input(" أدخل سؤالك هنا"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])
        
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("جارٍ التفكير..."):
            response = st.session_state.chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history        
# query = st.text_input("What would you like to know about your PDF?")
    
# if query:
#     print(type(query))
#     response = query_engine.query(query)
#     st.write(response)