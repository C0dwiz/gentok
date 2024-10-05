<h1 align="center">GenTok Library</h1>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0-blue" alt="Version">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
</p>

<p align="center">A Python library for generating and verifying secure tokens.</p>

<hr>

<h2>Overview</h2>

<p>Token Library is a Python library designed to generate and verify secure tokens. It uses a combination of random bytes and system information to create complex tokens that are difficult to forge.</p>

<h2>Features</h2>

<ul>
  <li><strong>Secure Token Generation:</strong> Generates complex tokens using random bytes and system information.</li>
  <li><strong>File-Based Token Storage:</strong> Saves tokens to files with the <code>.pkib</code> extension.</li>
  <li><strong>Token Verification:</strong> Validates tokens against stored values.</li>
</ul>

<h2>Installation</h2>

<p>To install the library, use pip. Navigate to the root directory of your project and run the following command:</p>

<pre><code>pip install .</code></pre>

<h2>Usage</h2>

<h3>Generating a New Token</h3>

<p>To generate a new token, use the <code>generate_token</code> function. The token will be saved to a file named <code>&lt;name&gt;.pkib</code>.</p>

<pre><code>from gentok import generate_token

# Generate a new token and save it to the file "test.pkib"
token = generate_token("test")
print("Generated Token:", token)
</code></pre>

<h3>Verifying a Token</h3>

<p>To verify a token, use the <code>check_token</code> function. This function checks if the provided token matches the token stored in the file <code>&lt;name&gt;.pkib</code>.</p>

<pre><code>from gentok import check_token

# Verify the token
is_valid = check_token("test", token)
print("Access granted." if is_valid else "Access denied.")
</code></pre>

<h3>Full Usage Example</h3>

<pre><code>from gentok import generate_token, check_token

# Generate a new token and save it to the file "test.pkib"
token = generate_token("test")
print("Generated Token:", token)

# Verify the token
is_valid = check_token("test", token)
print("Access granted." if is_valid else "Access denied.")
</code></pre>

<h2>Requirements</h2>

<p>Python 3.8 or higher</p>

<h2>License</h2>

<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>

<h2>Contributing</h2>

<p>Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.</p>

<h2>Contact</h2>

<p>For any questions or inquiries, please open an issue on GitHub.</p>

<hr>

<p align="center"><em>Thank you for using Token Library! We hope it makes your token management easier and more secure.</em></p>