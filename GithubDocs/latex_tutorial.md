Here are a few examples of Beamer slides with different features:

1. **Simple Presentation:**
   ```latex
   \documentclass{beamer}
   \begin{document}
   \begin{frame}
   \frametitle{Simple Presentation}
   Hello, world!
   \end{frame}
   \end{document}
   ```

2. **Slide with Bullet Points:**
   ```latex
   \documentclass{beamer}
   \begin{document}
   \begin{frame}
   \frametitle{Bullet Points}
   \begin{itemize}
   \item Point 1
   \item Point 2
   \item Point 3
   \end{itemize}
   \end{frame}
   \end{document}
   ```

3. **Slide with Columns:**
   ```latex
   \documentclass{beamer}
   \begin{document}
   \begin{frame}
   \frametitle{Columns}
   \begin{columns}
   \column{0.5\textwidth}
   This is some text in the first column.
   \column{0.5\textwidth}
   This is some text in the second column.
   \end{columns}
   \end{frame}
   \end{document}
   ```

4. **Slide with Images:**
   ```latex
   \documentclass{beamer}
   \begin{document}
   \begin{frame}
   \frametitle{Images}
   \begin{figure}
   \includegraphics[width=0.5\textwidth]{example-image}
   \caption{Example Image}
   \end{figure}
   \end{frame}
   \end{document}
   ```

5. **Slide with Math Equations:**
   ```latex
   \documentclass{beamer}
   \begin{document}
   \begin{frame}
   \frametitle{Math Equations}
   This is an equation: $E=mc^2$
   \end{frame}
   \end{document}
   ```

You can compile these examples using a LaTeX editor with Beamer support to see how they look as slides.