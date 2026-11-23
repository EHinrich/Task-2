#Аналитическое решение

$$
\frac{\partial^2 u(x, t)}{\partial t^2} - \frac{\partial^2 u(x, t)}{\partial x^2} + \sin u(x, t) = 0
$$

Тип волны:

$$
u(x, t) = A(t) f(x - vt)
$$

$$
\lim_{x \to -\infty} u(x, 0) = 0, \quad \lim_{x \to +\infty} u(x, 0) = 2\pi
$$

Так как

$$
\lim_{x \to +\infty} A(t) f(x - vt) = \text{const}, \quad \lim_{x \to -\infty} A(t) f(x - vt) = \text{const} \Rightarrow A(t) = \text{const}
$$

Пусть $`A(t) = 1`$:

$$
u(x, t) = f(x - vt)
$$

Замена $`\xi = x - vt`$:

$$
u(x, t) = f(\xi)
$$

$$
\frac{\partial^2 u}{\partial t^2} = \left(\frac{\partial u}{\partial t}\right)'_t = \left((-v)f'(\xi)\right)'_t = v^2 f''(\xi)
$$

$$
\frac{\partial^2 u}{\partial x^2} = f''(\xi)
$$

$$
v^2 f''(\xi) - f''(\xi) + \sin f(\xi) = 0
$$

$$
(v^2 - 1) f''(\xi) + \sin f(\xi) = 0 \quad \Big| \cdot f'(\xi)
$$


$$
\int \left((v^2 - 1) f''(\xi) f'(\xi) + f'(\xi) \sin f(\xi)\right) d\xi = 0
$$

$$
\frac{1}{2}(v^2 - 1)\left(f'(\xi)\right)^2 - \cos f(\xi) = C_1
$$

Так как $`\lim_{x \to \pm\infty} f(\xi) = \text{const} \Rightarrow \lim_{x \to \pm\infty} f'(\xi) = 0`$.

При $`x \to -\infty`$, $`f(x) \to 0`$:

$$
-\cos 0 = C_1 \Rightarrow C_1 = -1
$$

$$
\frac{1}{2}(v^2 - 1)\left(f'(\xi)\right)^2 = \cos f(\xi) - 1
$$

$$
\frac{v^2 - 1}{2}\left(f'(\xi)\right)^2 = -2\sin^2 \frac{f(\xi)}{2}
$$

$$
\left(f'(\xi)\right)^2 = -\frac{4}{v^2 - 1}\sin^2 \frac{f(\xi)}{2}
$$

$$
f'(\xi) = \sqrt{\frac{4}{1 - v^2}} \sin \frac{f(\xi)}{2}
$$

*(знак «+», т.к. решение возрастает)*

$$
\frac{df}{d\xi} = \frac{2}{\sqrt{1 - v^2}} \sin \frac{f}{2}
$$

$$
\frac{df}{\sin \dfrac{f}{2}} = \frac{2}{\sqrt{1 - v^2}}\, d\xi
$$


$$
\int \frac{df}{\sin \dfrac{f}{2}} = \frac{2}{\sqrt{1 - v^2}} \int d\xi
$$

$$
2\ln\left(\operatorname{tg}\frac{f}{4}\right) = \frac{2\xi}{\sqrt{1 - v^2}} + C
$$

$$
\ln\left(\operatorname{tg}\frac{f}{4}\right) = \frac{\xi}{\sqrt{1 - v^2}} + C
$$

$$
\operatorname{tg}\frac{f}{4} = C e^{\frac{\xi}{\sqrt{1 - v^2}}}
$$

$$
\frac{f}{4} = \operatorname{arctg}\left(C e^{\frac{\xi}{\sqrt{1 - v^2}}}\right)
$$

$$
f = 4\operatorname{arctg}\left(C \cdot e^{\frac{\xi}{\sqrt{1 - v^2}}}\right)
$$

$$
f(x - vt) = 4\operatorname{arctg}\left(C \cdot e^{\frac{x - vt}{\sqrt{1 - v^2}}}\right)
$$

$$
u(x, t) = 4\operatorname{arctg}\left(C e^{\frac{x - vt}{\sqrt{1 - v^2}}}\right)
$$
```[cite: 5, 6, 7]