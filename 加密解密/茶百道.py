import base64
import hashlib

# 原始数据
qm_user_csession = "1723258978|YmzHnxGDZ4YdJpj9.Wb3X346CVgF8yMszEEn4FhLQnBWQ8ChYVFnwlpK0Y9r8Zx8MGSrCn52P7Ugnx4V5sCTzLqWCzlZ/kB/Rl6X2OA==.6440369f99ac6bc4"

# 拆分数据
parts = qm_user_csession.split('|')
if len(parts) != 2:
    print("数据拆分错误：", parts)
else:
    timestamp = parts[0]  # 时间戳
    encoded_data_with_hash = parts[1]

    # 分离加密数据和哈希值
    split_hash = encoded_data_with_hash.rsplit('.', 1)
    if len(split_hash) != 2:
        print("分离加密数据和哈希值失败：", split_hash)
    else:
        encoded_data, expected_hash = split_hash

        # Base64 解码
        try:
            padded_encoded_data = encoded_data + "==" if len(encoded_data) % 4 else encoded_data
            decoded_data = base64.urlsafe_b64decode(padded_encoded_data)
            print(f"解码后的数据：{decoded_data}")
        except Exception as e:
            print(f"Base64 解码失败：{e}")

        # 打印解码后的数据长度和前几个字节
        print(f"解码后的数据长度：{len(decoded_data)}")
        print(f"解码后的数据前20个字节：{decoded_data[:20]}")

        # 计算不同哈希算法的哈希值
        def calculate_hash(data, algo='sha1'):
            if algo == 'sha1':
                hash_func = hashlib.sha1()
            elif algo == 'md5':
                hash_func = hashlib.md5()
            elif algo == 'sha256':
                hash_func = hashlib.sha256()
            else:
                raise ValueError("Unsupported hash algorithm")
            hash_func.update(data)
            return hash_func.hexdigest()

        # 校验哈希值
        for algo in ['sha1', 'md5', 'sha256']:
            calculated_hash = calculate_hash(decoded_data, algo)
            if calculated_hash == expected_hash:
                print(f"{algo.upper()} 哈希值校验通过: {calculated_hash}")
            else:
                print(f"{algo.upper()} 哈希值校验失败: {calculated_hash}, 预期: {expected_hash}")

        # 打印时间戳
        print(f"时间戳: {timestamp}")
