{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "\n",
    "### [17144. 미세먼지 안녕!](https://www.acmicpc.net/problem/17144)\n",
    "\n",
    "\n",
    "문제\n",
    "\n",
    "미세먼지를 제거하기 위해 구사과는 공기청정기를 설치하려고 한다. 공기청정기의 성능을 테스트하기 위해 구사과는 집을 크기가 R×C인 격자판으로 나타냈고, 1×1 크기의 칸으로 나눴다. 구사과는 뛰어난 코딩 실력을 이용해 각 칸 (r, c)에 있는 미세먼지의 양을 실시간으로 모니터링하는 시스템을 개발했다. (r, c)는 r행 c열을 의미한다.\n",
    "\n",
    "<img src=\"./img/17144_1.png\" width=\"60%\">\n",
    "\n",
    "\n",
    "공기청정기는 항상 1번 열에 설치되어 있고, 크기는 두 행을 차지한다. 공기청정기가 설치되어 있지 않은 칸에는 미세먼지가 있고, (r, c)에 있는 미세먼지의 양은 Ar,c이다.\n",
    "\n",
    "1초 동안 아래 적힌 일이 순서대로 일어난다.\n",
    "\n",
    "1. 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.\n",
    "    - (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.\n",
    "    - 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.\n",
    "    - 확산되는 양은 Ar,c/5이고 소수점은 버린다.\n",
    "    - (r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다.\n",
    "2. 공기청정기가 작동한다.\n",
    "    - 공기청정기에서는 바람이 나온다.\n",
    "    - 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.\n",
    "    - 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.\n",
    "    - 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.\n",
    "\n",
    "다음은 확산의 예시이다.\n",
    "\n",
    "<img src=\"./img/17144_2.png\" width=\"60%\">\n",
    "\n",
    "\n",
    "왼쪽과 위쪽에 칸이 없기 때문에, 두 방향으로만 확산이 일어났다.\n",
    "\n",
    "<img src=\"./img/17144_3.png\" width=\"60%\">\n",
    "\n",
    "인접한 네 방향으로 모두 확산이 일어난다.\n",
    "\n",
    "<img src=\"./img/17144_4.png\" width=\"60%\">\n",
    "\n",
    "공기청정기가 있는 칸으로는 확산이 일어나지 않는다.\n",
    "\n",
    "\n",
    "\n",
    "공기청정기의 바람은 다음과 같은 방향으로 순환한다.\n",
    "\n",
    "<img src=\"./img/17144_5.png\" width=\"60%\">\n",
    "\n",
    "방의 정보가 주어졌을 때, T초가 지난 후 구사과의 방에 남아있는 미세먼지의 양을 구해보자.\n",
    "\n",
    "입력\n",
    "\n",
    "    첫째 줄에 R, C, T (6 ≤ R, C ≤ 50, 1 ≤ T ≤ 1,000) 가 주어진다.\n",
    "\n",
    "    둘째 줄부터 R개의 줄에 Ar,c (-1 ≤ Ar,c ≤ 1,000)가 주어진다. 공기청정기가 설치된 곳은 Ar,c가 -1이고, 나머지 값은 미세먼지의 양이다. -1은 2번 위아래로 붙어져 있고, 가장 윗 행, 아랫 행과 두 칸이상 떨어져 있다.\n",
    "\n",
    "출력\n",
    "\n",
    "    첫째 줄에 T초가 지난 후 구사과 방에 남아있는 미세먼지의 양을 출력한다.\n",
    "\n",
    "예제 입력 1 \n",
    "\n",
    "    7 8 1\n",
    "    0 0 0 0 0 0 0 9\n",
    "    0 0 0 0 3 0 0 8\n",
    "    -1 0 5 0 0 0 22 0\n",
    "    -1 8 0 0 0 0 0 0\n",
    "    0 0 0 0 0 10 43 0\n",
    "    0 0 5 0 15 0 0 0\n",
    "    0 0 40 0 0 0 20 0\n",
    "\n",
    "예제 출력 1 \n",
    "\n",
    "    188\n",
    "\n",
    "미세먼지의 확산이 일어나면 다음과 같은 상태가 된다. \n",
    "\n",
    "<img src=\"./img/17144_6.png\" width=\"60%\">\n",
    "\n",
    "공기청정기가 작동한 이후 상태는 아래와 같다.\n",
    "\n",
    "<img src=\"./img/17144_7.png\" width=\"60%\">"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 예제 더보기"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "예제 입력 2 \n",
    "\n",
    "    7 8 2\n",
    "    0 0 0 0 0 0 0 9\n",
    "    0 0 0 0 3 0 0 8\n",
    "    -1 0 5 0 0 0 22 0\n",
    "    -1 8 0 0 0 0 0 0\n",
    "    0 0 0 0 0 10 43 0\n",
    "    0 0 5 0 15 0 0 0\n",
    "    0 0 40 0 0 0 20 0\n",
    "\n",
    "예제 출력 2 \n",
    "\n",
    "    188\n",
    "\n",
    "예제 입력 3 \n",
    "\n",
    "    7 8 3\n",
    "    0 0 0 0 0 0 0 9\n",
    "    0 0 0 0 3 0 0 8\n",
    "    -1 0 5 0 0 0 22 0\n",
    "    -1 8 0 0 0 0 0 0\n",
    "    0 0 0 0 0 10 43 0\n",
    "    0 0 5 0 15 0 0 0\n",
    "    0 0 40 0 0 0 20 0\n",
    "\n",
    "예제 출력 3 \n",
    "\n",
    "    186\n",
    "\n",
    "예제 입력 4 \n",
    "\n",
    "    7 8 4\n",
    "    0 0 0 0 0 0 0 9\n",
    "    0 0 0 0 3 0 0 8\n",
    "    -1 0 5 0 0 0 22 0\n",
    "    -1 8 0 0 0 0 0 0\n",
    "    0 0 0 0 0 10 43 0\n",
    "    0 0 5 0 15 0 0 0\n",
    "    0 0 40 0 0 0 20 0\n",
    "\n",
    "예제 출력 4 \n",
    "\n",
    "    178\n",
    "\n",
    "예제 입력 5 \n",
    "\n",
    "    7 8 5\n",
    "    0 0 0 0 0 0 0 9\n",
    "    0 0 0 0 3 0 0 8\n",
    "    -1 0 5 0 0 0 22 0\n",
    "    -1 8 0 0 0 0 0 0\n",
    "    0 0 0 0 0 10 43 0\n",
    "    0 0 5 0 15 0 0 0\n",
    "    0 0 40 0 0 0 20 0\n",
    "\n",
    "예제 출력 5 \n",
    "\n",
    "    172\n",
    "\n",
    "예제 입력 6 \n",
    "\n",
    "    7 8 20\n",
    "    0 0 0 0 0 0 0 9\n",
    "    0 0 0 0 3 0 0 8\n",
    "    -1 0 5 0 0 0 22 0\n",
    "    -1 8 0 0 0 0 0 0\n",
    "    0 0 0 0 0 10 43 0\n",
    "    0 0 5 0 15 0 0 0\n",
    "    0 0 40 0 0 0 20 0\n",
    "\n",
    "예제 출력 6 \n",
    "\n",
    "    71\n",
    "\n",
    "예제 입력 7 \n",
    "\n",
    "    7 8 30\n",
    "    0 0 0 0 0 0 0 9\n",
    "    0 0 0 0 3 0 0 8\n",
    "    -1 0 5 0 0 0 22 0\n",
    "    -1 8 0 0 0 0 0 0\n",
    "    0 0 0 0 0 10 43 0\n",
    "    0 0 5 0 15 0 0 0\n",
    "    0 0 40 0 0 0 20 0\n",
    "\n",
    "예제 출력 7 \n",
    "\n",
    "    52\n",
    "\n",
    "예제 입력 8 \n",
    "\n",
    "    7 8 50\n",
    "    0 0 0 0 0 0 0 9\n",
    "    0 0 0 0 3 0 0 8\n",
    "    -1 0 5 0 0 0 22 0\n",
    "    -1 8 0 0 0 0 0 0\n",
    "    0 0 0 0 0 10 43 0\n",
    "    0 0 5 0 15 0 0 0\n",
    "    0 0 40 0 0 0 20 0\n",
    "\n",
    "예제 출력 8 \n",
    "\n",
    "    46\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 코드"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
