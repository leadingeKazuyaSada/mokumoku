-- グローバル変数 Foo に空のハッシュをセット
-- これがクラスみたいなもの (Lua にクラスはないらしい)
Foo = {}

-- Foo の new というフィールドに関数をセットする
-- これがコンストラクタとなる
function Foo.new(a, b)
    return {
        a = a,
        b = b,
        get_a = function(self) return self.a end,
        get_b = function(self) return self.b end
    }
end

local x = Foo.new(10, 20)
print('x.a => '..x.a)

-- 自身を第1引数 (self) に渡すには、コロン + メソッド名とする
print('x:get_a() => '..x:get_a())
