
namespace Assign_1._2___WF_Hello_World
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.mainbutton = new System.Windows.Forms.Button();
            this.maintextbox = new System.Windows.Forms.TextBox();
            this.mainlabel = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // mainbutton
            // 
            this.mainbutton.Location = new System.Drawing.Point(194, 71);
            this.mainbutton.Name = "mainbutton";
            this.mainbutton.Size = new System.Drawing.Size(75, 23);
            this.mainbutton.TabIndex = 0;
            this.mainbutton.Text = "Change";
            this.mainbutton.UseVisualStyleBackColor = true;
            this.mainbutton.Click += new System.EventHandler(this.mainbutton_Click);
            // 
            // maintextbox
            // 
            this.maintextbox.Location = new System.Drawing.Point(12, 74);
            this.maintextbox.Name = "maintextbox";
            this.maintextbox.Size = new System.Drawing.Size(168, 20);
            this.maintextbox.TabIndex = 1;
            // 
            // mainlabel
            // 
            this.mainlabel.AutoSize = true;
            this.mainlabel.Location = new System.Drawing.Point(12, 9);
            this.mainlabel.Name = "mainlabel";
            this.mainlabel.Size = new System.Drawing.Size(51, 13);
            this.mainlabel.TabIndex = 2;
            this.mainlabel.Text = "mainlabel";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(281, 106);
            this.Controls.Add(this.mainlabel);
            this.Controls.Add(this.maintextbox);
            this.Controls.Add(this.mainbutton);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button mainbutton;
        private System.Windows.Forms.TextBox maintextbox;
        private System.Windows.Forms.Label mainlabel;
    }
}

