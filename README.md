# DjangoCupcakeshop 파이콘장고튜토리얼

<img src="https://lh3.googleusercontent.com/zVZLq7583lOJ9Q7eddqoqjhk1nc1pwvjqvKulHO5DRkA0iuRNbvX_WeWDXh2BaCAan72N9CT9zfH=w240-h159-no">

## Brief Introduction
If you want to get started with Django, there is a great official Django tutorial you can try. Unfortunately, it is written for people having some prior web programming experience. But there is an easy version of it written for beginners with all the installation steps included. If you guessed it right, it is Django Girls Tutorial. You might have tried it at home, but not sure how to start your own project. This tutorial will walk you through all the steps in creating a Cupcake shop menu site (DjangoCupcake Shop). By the end, you'll be confident enough to make your website! Cupcakes and high fives!

장고가 처음이시라면, 공식 장고 튜토리얼 문서를 보시는 것이 가장 좋습니다.  장고 튜토리얼 문서는 웹 프로그래밍 경험이 있는 사람들을 위해 작성되었습니다. 그러나 입문자를 대상으로 모든 설치 방법과 과정이 설명된 쉬운 튜토리얼도 있지요. 네, 모두가 알고 계시는 바로 장고걸스 튜토리얼 입니다. 아마 이 글을 읽으시는 많은 분들이 집에서 장고걸스 튜토리얼을 해보셨겠지만, 어디서 부터 내 개인프로젝트를 시작할지 감이 안오실 텐데요. 이번 파이콘에서 함께하는 이 튜토리얼에서는 컵케이크 가게 메뉴 사이트를 만드는 모든 과정을 실습해 볼 예정입니다. 이를 통해 여러분은 웹사이트를 만들 수 있다는 자신감을 가지게 되실 거에요! 컵케이크와 하이파이브 해봅시다!


## Detailed description

### Introduction
**Django** is a large and sometimes complex framework for building web applications and sites using the popular programming language, Python. For many beginners, once they complete the Django tutorial, the next step is unknown. They are unsure how to start their own website. The purpose of this tutorial to guide through all the steps involved in creating a new website project from scratch.For this tutorial, you can fork repository and then clone it to get the starting code. Follow along tutor for live coding.

장고(쟁고: Django)는 전 세계에서 가장 인기 있는 언어인 파이썬으로 작성된 웹 어플리케이션과 사이트 개발을 위한 프레임워크로 그 범위가 매우 크고 복잡합니다. 장고튜토리얼을 한번 마친 입문자들의 경우, 그 다음 무엇을 만들어봐야할지 막막하기만 합니다. 나만의 웹사이트를 만들기 위해 어디서부터  시작해야할까요? 우리는 튜토리얼에서 이미 어느정도 만들어진 리퍼지토리를 깃헙에서 다운 받아 여러 기능을 추가하고 소스 코드를 조금씩 수정해보면서 장고 웹프레임워크을 활용한 웹 개발 과정을 조금씩 맛보고자 합니다.


### Brief Description:

Inspired from Django Girls **'Cupcakes and high fives'** expression at end of every email, We will build a cupcake menu website called DjangoCupcake Shop[[Github](https://github.com/DjangoGirlsSeoul/djangocupcakeshop)]. We will also look into how to create a virtual environment and `pip install django` and other packages. What goes inside a model, how to create an ImageField and how to add a model form for allowing users to add data. Finally, we will deploy our site on PythonAnywhere and Azure(if time available) for whole world to see it!

장고걸스에서는 모든 이메일 끝에 ‘컵케이크와 하이파이브!’(Cupcakes and high fives) 라는 메세지를  붙입니다. 그래서 우리가 만들 사이트는 바로 장고컵케이크샵[Github]입니다. 가상환경과 `pip install django`, 그리고 다른 패키지들을 생성하는 방법을 살펴볼 것입니다. 모델에서는 이미지 입력(ImageField)과 사용자가 데이터를 입력하는 모델 폼을 추가하는 방법을 알아 볼 것입니다. 마지막으로 시간이 허락된다면, 만든 여러분의 사이트를 PythonAnywhere 또는 Azure를 배포해 전 세계 모든 사람들이 볼 수 있도록 해볼 것입니다!


### Prerequisites:

While beginners are welcome for this tutorial, we recommend completing installation of Python, Django and code Editor beforehand. This tutorial also assumes that you have already tried either Django Girls Tutorial or any other Django tutorial and know basics of Python. You can follow these links [[English](http://tutorial.djangogirls.org/en/installation/) , [Korean](https://djangogirlsseoul.gitbooks.io/tutorial/content/installation/)] for detailed guideline.

The primary language of instruction will be **English** however the tutorial itself is available in Korean!  Please bring your computer with battery fully charged!

### 준비 사항

이 튜토리얼은 초보자를 환영합니다. 좀더 나은 실습환경을 위해 미리 파이썬, 장고, 코드 에디터를 설치해오세요. 미리 장고걸스튜토리얼, 장고 공식 튜토리얼, 파이썬 기초 등을 학습하시고 오셔도 좋습니다. 다음 링크 [영어, 한국어]에서 도움을 받으실 수 있습니다.
튜로리얼 진행은 영어로 진행이 될 것이지만

### Specific Goals for this tutorial:

- The learners should be able to use virtual environment correctly before starting any Django project.
- The learners should be able to use ImageField in model.
- The leaners should be able understand role of admin in Django.
- The learners should able to make base templates and extend other templates from base template.
- The learners should be able to create a model form and add it to template.
- The learners should be able to use Git/Github basic commands for adding their project on github
- The learners should be able to deploy their site on PythonAnywhere server with DEBUG=False mode.
- The learners should be able to write simple test for their Django site.

### Detailed Steps:

Follow this [link](https://www.gitbook.com/book/djangogirlsseoul/-djangocupcakeshop/details) along tutor for step by step guide.

### Contributors

Hassan Abid, Jin Park, Soeun Lee, Sujin Lee

### 도움주신 분들

**장고걸스서울의 운영진과 코치들이 함께 튜토리얼을 준비했습니다**
하산 아비드, 박진우, 이소은, 이수진
