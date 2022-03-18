-- グローバル変数 Foo に空のハッシュをセット
-- これがクラスみたいなもの (Lua にクラスはないらしい)
Foo = {}

-- メソッド定義 (1箇所で定義してインスタンスから参照)
-- Foo:get_a() のようにコロンを使って self を省略可能
function Foo.get_a(self) return self.a end
function Foo.get_b(self) return self.b end
function Foo.set_a(self, x) self.a = x end
function Foo.set_b(self, x) self.b = x end

-- コンストラクタ
function Foo.new(a, b)
  local obj = {a = a, b = b}

  -- メタテーブルをセットして obj を返す
  return setmetatable(obj, {__index = Foo})
end

local x = Foo.new(10, 20)
x:set_a(30)
print('x:get_a() => '..x:get_a())
