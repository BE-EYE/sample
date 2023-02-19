# KeyBert

## BERT

> (Bidirectional Encoder Representations from Transformers)

2018년에 자연어 처리를 위해 구글에서 고안한 트랜스포머 기반의 머신러닝 기법. BERT의 가장 큰 특징은 **문장 전체의 구조를 양방향으로 학습**하여 문맥을 파악할 수 있다는 것이다. 같은 단어인 경우에도 앞뒤 문맥을 통해 구분이 가능한 것이다.

<br>

## KeyBERT

> BERT를 적용한 오픈 소스 파이썬 모듈인 KeyBERT

BERT를 이용해 문서 레벨 (document-level)에서의 주제 (representation)를 파악하고, N-gram을 위해 단어를 임베딩한다. 이후 코사인 유사도를 계산하여 어떤 N-gram 단어 또는 구가 문서와 가장 유사한지 찾아낸다. 가장 유사한 단어들은 문서를 가장 잘 설명할 수 있는 키워드로 분류된다.

<hr>

## 참고자료

- [keybert로-관련-키워드-추출하기](https://insightcampus.co.kr/2021/07/08/keybert%EB%A1%9C-%EA%B4%80%EB%A0%A8-%ED%82%A4%EC%9B%8C%EB%93%9C-%EC%B6%94%EC%B6%9C%ED%95%98%EA%B8%B0/)
- [BERT를 이용한 키워드 추출 : 키버트(KeyBERT)](https://wikidocs.net/159467)
- [BERT-keyBert로-키워드-추출하기](https://velog.io/@mare-solis/BERT-keyBert%EB%A1%9C-%ED%82%A4%EC%9B%8C%EB%93%9C-%EC%B6%94%EC%B6%9C%ED%95%98%EA%B8%B0)
- [Github - MaartenGr/KeyBERT](https://maartengr.github.io/KeyBERT/index.html)
