# デザインパターン

プログラム参考：[デザインパターンの解説と実装例！](https://www.mum-meblog.com/entry/study/design-pattern)

勉強としてデザインパターンをPythonで実装してみる

## Strategyパターン

参考：[TECHSCORE](https://www.techscore.com/tech/DesignPattern/Strategy)

メソッドの中にアルゴリズムが溶け込んで、if文などで切り替えなくても、戦略と部分を別クラスで用意しておき、戦略を変更したいときに利用する戦略クラスを切り替えることで、変更する方法。メンテナンスがしやすい。

## Decoratorパターン

動的にオブジェクトをラップすることで、メソッドの動きを追加することができる。

[TECHSCORE](https://www.techscore.com/tech/DesignPattern/Decorator)より：  
デコレータパターンは飾り枠と中身を同一視しして、機能を被せて実装していくイメージ。

[Qiita：Pythonで、デザインパターン「Decorator」を学ぶ](https://qiita.com/ttsubo/items/6f1569425644054dd079)より  
既存のオブジェクトに、新しい機能や振る舞いを動的に追加していく。イメージとしては、スポンジケーキのようなコンポーネントを用意して、その上に装飾（デコレータ）を追加していくことで、動的に機能を追加してくデザインパターン

## Commandパターン

操作をオブジェクトとしてカプセル化することで、一連の動作を１つのコマンドで管理することができる。
